import speech_recognition as sr
import os 
import numpy as np
from pydub import AudioSegment
from pydub.silence import split_on_silence
from datetime import datetime

def generate_statistics(actual_text, wav_file, transcriber='sphinx'):
    """
    Generates statistics to upload to mongodb:

    {
        screen_text: actual_text
        ouput_text: output of transcription
        time_taken: audio length of transcription, in seconds
        words_spoken: number of words spoken
        correct_words_spoken: number of correct words spoken
        total_words_per_second: words_spoken / time_taken
        correct_words_per_second: correct_words_spoken / time_taken
        accuracy: accuracy of the transcribed text
    }
    
    Arguments:
        actual_text: a string of the actual text
        wav_file: a string with the path to the .wav file
    Returns:
        an object with the statistics
    """

    transcribed_text, audio_length = transcribe(wav_file, transcriber)
    transcribed_list = sentence_to_word_list(transcribed_text)
    actual_list = sentence_to_word_list(actual_text)

    matches, match_indeces = matching_words(actual_list, transcribed_list)
    accuracy_val = accuracy(actual_list, transcribed_list, matches)
    words_spoken = len(transcribed_list)

    data = {}
    data['screen_text'] = actual_text
    data['ouput_text'] = transcribed_text
    data['time_taken'] = audio_length
    data['words_spoken'] = words_spoken
    data['correct_words_spoken'] = matches
    data['total_words_per_second'] = words_spoken / audio_length
    data['correct_words_per_second'] = matches / audio_length
    data['accuracy'] = accuracy_val * 100
    data['time_created'] = datetime.now()
    return data

def accuracy(actual: list[str], transcribed: list[str], matches: int) -> float:
    """
    Returns the accuracy between the actual and transcribed texts

    The accuracy the minimum between [matches / number of actual words] and [matches / number of transcribed words]
    
    Arguments:
        actual: a list of the actual words
        transcribed: a list of the transcribed words
        matchs: number of matches between the actual and transcribed lists
    Returns:
        a number between 0 and 1 representing the accuracy of the transcribed words
    """
    if len(transcribed) == 0 or len(actual) == 0:
        return 0.0
    
    return min(matches / len(actual), matches / len(transcribed))

def sentence_to_word_list(sentence):
    """
    Given a sentence, returns a list with the words in lowercase
    
    Arguments:
        sentence: a string
    Returns:
        a list of the words in the sentence, in lowercase
    """
    punctuation = ['.', ',', '!', '?', ':', ';']
    sentence = sentence.lower()
    for p in punctuation:
        sentence = sentence.replace(p, "")
    return sentence.split()

def list_find(list, value, start):
    """
    Returns the first index of a value in a numpy array, or -1 if there is none
    
    Arguments:
        list: a numpy array
        value: the value to search for
        start: the starting point to search the array
    Returns:
        The first index of value in list, or -1 if there is none
    """
    i_list = np.where(list[start:] == value)[0]
    if len(i_list) == 0:
        return -1
    return i_list[0] + start

def matching_words(main, secondary):
    """
    Given two word lists, return the number of matching words and the matching indeces in the main list

    A subsequence of the main list is considered to match the secondary array if:\n
        Every element in the subsequence has a match in the secondary array; and\n
        The matches in the secondary array also form a subsequence\n

    This function chooses the largest of such subsequences
    
    Arguments:
        main: a word list
        secondary: a word list
    Returns:
        matching: number of matching elements
        indeces: list of indeces corresponding to the matching elements in the main list
    """
    main_np = np.array(main)
    sec_np = np.array(secondary)
    arr = np.zeros((len(main_np) + 1, len(sec_np) + 1))

    for i in range(len(main_np)-1, -1, -1):
        word = main_np[i]
        for j in range(len(sec_np)):
            index = list_find(sec_np, word, j)
            if index == -1:
                arr[i][j] = arr[i+1][j]
            else:
                arr[i][j] = max(arr[i+1][j], arr[i+1][index+1]+1)
    
    index = 0
    indeces = []
    for i in range(len(main_np)):
        if arr[i][index] != arr[i+1][index]:
            indeces.append(i)
            index = list_find(sec_np, main_np[i], index) + 1
    
    matching = int(arr[0][0])

    return matching, indeces

def transcribe(wav_file, transcriber='sphinx'):
    """
    Transcribes an audio file
    
    Arguments:
        wav_file: a string with the path to the .wav file
    Returns:
        text: the transcribed file
        audio_length: the length of the audio file, in seconds
    """

    r = sr.Recognizer()
    transcriber_dict = {
        'google': r.recognize_google,
        'sphinx': r.recognize_sphinx
    }

    transcriber_method = transcriber_dict[transcriber]
    
    sound = AudioSegment.from_wav(wav_file)  
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-14,
        keep_silence = 500,
    )
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    text = ""
    audio_length = 0
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                cur_text = transcriber_method(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                cur_text = f"{cur_text.capitalize()}. "
                text += cur_text
                audio_length += len(audio_listened.frame_data) / (audio_listened.sample_rate * audio_listened.sample_width)
        os.remove(chunk_filename)
    os.rmdir(folder_name)
    text = text.strip()
    return text, audio_length

