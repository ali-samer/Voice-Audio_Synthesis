import sounddevice as sd
import soundfile as sf


def play_audio_async(filename):
    """
    Play an audio file asynchronously using the sounddevice library.

    Parameters:
    - filename (str): Path to the audio file to be played.

    Returns:
    - data: Audio data read from the file.
    - fs: Sampling frequency of the audio data.

    Example:
    data, fs = play_audio_async('play.wav')
    """
    data, fs = sf.read(filename)
    sd.play(data, fs)
    return data, fs


# Example usage:
"""
data, fs = play_audio_async('play.wav')

# You can execute commands while audio is playing
print('Able to execute this before finishing')
print('Hi, this is cool!')

# You can stop playback after 1 second
time.sleep(1)
sd.stop()
print('Stopped')
"""
