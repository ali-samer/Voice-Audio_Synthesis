import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os
import json
import datetime
import threading
import sys
import time

# Function to animate the "Recording..." message in a separate thread
def animate_recording_message():
    while not recording_done_event.is_set():
        sys.stdout.write("\rRecording...")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\rRecording..")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\rRecording.")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rRecording done.\n")

def record_audio(filename, duration, sample_rate, num_channels):
    """
    Record audio and save it to a file.

    Parameters:
    - filename (str): Name of the output audio file.
    - duration (float): Duration of the recording in seconds.
    - sample_rate (int): Sampling rate (e.g., 16000 for 16 kHz).
    - num_channels (int): Number of audio channels (e.g., 1 for mono).

    Example:
    record_audio('sync_record.wav', 10, 16000, 1)
    """
    global recording_done_event
    recording_done_event = threading.Event()

    # Start the recording animation thread
    animation_thread = threading.Thread(target=animate_recording_message)
    animation_thread.start()

    myrecording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=num_channels)
    sd.wait()
    sf.write(filename, myrecording, sample_rate)

    # Set the recording_done_event to stop the animation
    recording_done_event.set()
    animation_thread.join()

def transcribe_audio(filename):
    """
    Transcribe audio using PocketSphinx.

    Parameters:
    - filename (str): Name of the input audio file.

    Returns:
    - str: Transcription text.

    Example:
    transcript = transcribe_audio('sync_record.wav')
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_sphinx(audio)
    print('Transcript: ' + text)
    return text

def store_transcript(filename, transcript):
    """
    Store the transcription in a JSON file.

    Parameters:
    - filename (str): Name of the audio file.
    - transcript (str): Transcription text.

    Example:
    store_transcript('sync_record.wav', transcript)
    """
    json_filename = filename[:-4] + '.json'
    print(f'Saving {json_filename} to the current directory')
    data = {
        'date': str(datetime.datetime.now()),
        'filename': filename,
        'transcript': transcript,
    }
    print(data)
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)

# Record audio and transcribe it
filename = 'sync_record.wav'
record_audio(filename, 10, 16000, 1)
transcript = transcribe_audio(filename)
store_transcript(filename, transcript)
