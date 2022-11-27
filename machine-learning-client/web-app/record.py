from flask import render_template, request, redirect, url_for
import utils
from db import recordings_collection

def record():
  """
  Route for POST requests to the recoding page
  Accepts the form submission data for a new recording
  """
  if request.method == "POST":
    try:
      recording = recording_object(request.form, request.files)
      result = recordings_collection.insert_one(recording)
      return redirect(url_for('results', id=str(result.inserted_id)))
    except ValueError as ve:
      return str(ve), 400
    except Exception as e:
      return str(e), 500
  else:
    return render_template('record.html')
  
def recording_object(form, files):
  """
  Create a recording object from the form data and files
  """
  reqs = ['name', 'text', 'recording', 'transcription']
  for req in reqs:
    if req not in form:
      raise ValueError('Missing required field: %s' % req)
  
  audio_file = []
  if ('recording' in files) and (request.files['recordings'].filename != ''):
    recordings = files.getlist('recordings')
    for recording in recordings:
      if utils.is_file_audio(recording.filename):
        audio_file.append(recording.read())
      else:
        raise ValueError('File %s is not audio' % recording.filename)
  return {
    "name": form.get('name'),
    "text": form.get('text'),
    "recording": audio_file,
    "transcription": form.get('transcription'),
  }