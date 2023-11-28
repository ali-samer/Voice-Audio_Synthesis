import sounddevice as sd
import soundfile as sf
import time
import threading
import sys

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

def record_audio_async(filename, duration_seconds, sample_rate, num_channels):
    """
    Record audio asynchronously and save it to a file.

    Parameters:
    - filename (str): Path to the output audio file.
    - duration_seconds (float): Duration of the recording in seconds.
    - sample_rate (int): Sampling rate (e.g., 16000 for 16 kHz).
    - num_channels (int): Number of audio channels (e.g., 1 for mono).

    Example:
    # record_audio_async('async_record.wav', 10, 16000, 1)
    """
    global recording_done_event
    recording_done_event = threading.Event()

    # Start the recording animation thread
    animation_thread = threading.Thread(target=animate_recording_message)
    animation_thread.start()

    print('Recording', end='')

    recording = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=num_channels)
    print('Able to execute commands before finishing')
    sd.wait()
    sf.write(filename, recording, sample_rate)

    # Set the recording_done_event to stop the animation
    recording_done_event.set()
    animation_thread.join()

    print('Recording done.')

# Example usage:
# record_audio_async('async_record.wav', 10, 16000, 1)
