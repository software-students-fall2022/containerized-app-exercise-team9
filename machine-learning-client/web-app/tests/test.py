import pytest
import sys
import numpy as np
import transcribe_audio as transcribe

class Tests:
    def sanity_check(self):
        """
        Throwaway test.
        """
        expected = True
        actual = True
        assert expected == actual
    
    def test_no_wav_file(self):
        """
        Testing if error is raised when a non-wav file is used.
        """
        with pytest.raises(FileNotFoundError) as err:
            transcribe.transcribe("")

    def test_short_transcription(self):
        """
        Testing if correctly transcribes short audio
        """
        transcribed, _ = transcribe.transcribe("tests/test_short.wav")
        assert transcribed == "Hello world.", f"Expected transcription to return 'Hello world.' instead it returned {transcribed}"

    def test_generate_statistics(self):
        """
        Testing if correctly generates mongodb data from short audio
        """
        data = transcribe.generate_statistics("Hello world.", "tests/test_short.wav")

        assert data['screen_text'] == "Hello world.", f"Expected screen_text to be 'Hello world.', instead it was '{data['screen_text']}'"

        assert data['ouput_text'] == "Hello world.", f"Expected output_text to be 'Hello world.', instead it was '{data['output_text']}'"

        assert data['time_taken'] >= 1 and data['time_taken'] <= 1.5, f"Expected time_taken to be between 1 and 1.5, instead it was {data['time_taken']}"
        
        assert data['words_spoken'] == 2, f"Expected words_spoken to be 2, instead it was {data['words_spoken']}"
        
        assert data['correct_words_spoken'] == 2, f"Expected correct_words_spoken to be 2, instead it was {data['correct_words_spoken']}"
        
        assert data['total_words_per_second'] == data['words_spoken'] / data['time_taken'], f"Expected total_words_per_second to be {data['words_spoken'] / data['time_taken']}, instead it was {data['total_words_per_second']}"
        
        assert data['correct_words_per_second'] == data['correct_words_spoken'] / data['time_taken'], f"Expected correct_words_per_second to be {data['correct_words_spoken'] / data['time_taken']}, instead it was {data['correct_words_per_second']}"
        
        assert data['accuracy'] == 100.0, f"Expected accuracy to be 1.0, instead it was {data['accuracy']}"

    def test_audio_length(self):
        """
        Testing if correctly gets audio length
        """
        _, audio_length = transcribe.transcribe("tests/test_short.wav")
        assert audio_length >= 1 and audio_length <= 1.5, f"Error, expected audio length to be between 64 and 65, instead it was {audio_length}"

    def test_sentence_to_word_list(self):
        """
        Tests if sentence_to_word_list() correctly returns a word list
        """
        sentence = "Hello world! What a lovely day this is, isn't it?"
        expected = ["hello", "world", "what", "a", "lovely", "day", "this", "is", "isn't", "it"]
        actual = transcribe.sentence_to_word_list(sentence)
        assert expected == actual, f"Expected word list to be {expected}, instead, it was {actual}"
    
    def test_list_find(self):
        """
        Tests if list_find() correctly returns the index of a value in a numpy array
        """
        np_list = np.array(["a", "b", "c", "d", "e"])

        test_array = [
            {'value': "a", 'start': 0, 'expected': 0},
            {'value': "c", 'start': 0, 'expected': 2},
            {'value': "c", 'start': 2, 'expected': 2},
            {'value': "c", 'start': 3, 'expected': -1},
            {'value': "f", 'start': 0, 'expected': -1},
        ]

        for test in test_array:
            value = test['value']
            start = test['start']
            expected = test['expected']
            actual = transcribe.list_find(np_list, value, start)
            assert expected == actual, f"Expected list_find with list={np_list}, value={value}, start={start} to return {expected}, instead it returned {actual}"
    
    def test_accuracy(self):
        """
        Tests if accuracy() correctly returns the correct accuracies
        """

        text = ['a', 'b']
        transcribed = ['a', 'b']
        matches = 2
        expected = 1.0
        actual = transcribe.accuracy(text, transcribed, matches)
        assert expected == actual, f"Expected accuracy between {text} and {transcribed} to be {expected}. Instead, it was {actual}."

        text = ['a', 'b']
        transcribed = ['a']
        matches = 1
        expected = 0.5
        actual = transcribe.accuracy(text, transcribed, matches)
        assert expected == actual, f"Expected accuracy between {text} and {transcribed} to be {expected}. Instead, it was {actual}."

        text = ['a']
        transcribed = ['a', 'b']
        matches = 1
        expected = 0.5
        actual = transcribe.accuracy(text, transcribed, matches)
        assert expected == actual, f"Expected accuracy between {text} and {transcribed} to be {expected}. Instead, it was {actual}."

        text = ['a', 'b']
        transcribed = []
        matches = 0
        expected = 0.0
        actual = transcribe.accuracy(text, transcribed, matches)
        assert expected == actual, f"Expected accuracy between {text} and {transcribed} to be {expected}. Instead, it was {actual}."
    
    def all_matching_words(self):
        """
        """
        main = ['hello', 'world', 'what', 'a', 'lovely', 'day', 'we', 'are', 'having']
        secondary = ['hello', 'world', 'what', 'a', 'lovely', 'day', 'we', 'are', 'having']
        assert transcribe.matching_words(main, secondary) == [len(main), [0, 1, 2, 3, 4, 5, 6, 7, 8]]
    
    def some_matching_words(self):
        """
        """
        main = ['hello', 'world', 'what', 'a', 'lovely', 'day', 'we', 'are', 'having']
        secondary = ['hello', 'world', 'you', 'are', 'lovely']
        matches = 3
        assert transcribe.matching_words(main, secondary) == [matches, [0, 1, 4]]
    
    def no_matching_words(self):
        """
        """
        main = ['hello', 'world', 'what', 'a', 'lovely', 'day', 'we', 'are', 'having']
        secondary = ['i', 'am', 'getting', 'bad', 'sleep', 'these', 'days']
        assert transcribe.matching_words(main, secondary) == [0, []]