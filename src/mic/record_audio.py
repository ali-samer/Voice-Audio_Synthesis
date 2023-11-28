import sounddevice as sd
import soundfile as sf
import time

def record_audio(filename, duration_seconds, sample_rate, num_channels):
    """
    Record audio synchronously and save it to a file.

    Parameters:
    - filename (str): Path to the output audio file.
    - duration_seconds (float): Duration of the recording in seconds.
    - sample_rate (int): Sampling rate (e.g., 16000 for 16 kHz).
    - num_channels (int): Number of audio channels (e.g., 1 for mono).

    Example:
    record_audio_sync('sync_record.wav', 10, 16000, 1)
    """
    print('Recording', end='')
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(1)
    print('')  # Print a newline after the dots

    recording = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=num_channels)
    sd.wait()
    sf.write(filename, recording, sample_rate)
    print('Recording done.')

# Example usage:
# record_audio('sync_record.wav', 10, 16000, 1)
