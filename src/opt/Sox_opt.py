import os

import os

def concat_audio(in_file1, in_file2, out_file):
    """
    Concatenate two audio files.

    Parameters:
    - in_file1 (str): Path to the first input audio file.
    - in_file2 (str): Path to the second input audio file.
    - out_file (str): Path to the output concatenated audio file.

    Example:
    concat_audio("one.wav", "two.wav", "three.wav")
    """
    os.system(f'sox {in_file1} {in_file2} {out_file}')

def trim_audio(input_file, output_file, start_time, duration):
    """
    Trim an audio file.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the trimmed output audio file.
    - start_time (float): Starting time in seconds for the trim.
    - duration (float): Duration in seconds to keep in the trimmed audio.

    Example:
    trim_audio("one.wav", "output.wav", 0, 1)
    """
    os.system(f'sox {input_file} {output_file} trim {start_time} {duration}')

def adjust_volume(input_file, output_file, volume_factor):
    """
    Adjust the volume of an audio file.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output audio file with adjusted volume.
    - volume_factor (float): Volume scaling factor (e.g., 2.0 for doubling volume, 0.5 for halving).

    Example:
    adjust_volume("one.wav", "volup.wav", 2.0)
    """
    os.system(f'sox -v {volume_factor} {input_file} {output_file}')

def reverse_audio(input_file, output_file):
    """
    Reverse an audio file.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the reversed output audio file.

    Example:
    reverse_audio("one.wav", "reverse.wav")
    """
    os.system(f'sox {input_file} {output_file} reverse')

def change_sample_rate(input_file, output_file, new_sample_rate):
    """
    Change the sample rate of an audio file.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output audio file with the new sample rate.
    - new_sample_rate (int): Desired new sample rate in Hz.

    Example:
    change_sample_rate("one.wav", "sr.wav", 16000)
    """
    os.system(f'sox {input_file} -r {new_sample_rate} {output_file}')

def change_audio_quality(input_file, output_file, bits_per_sample):
    """
    Change the audio quality (bit depth) of an audio file.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output audio file with the new bit depth.
    - bits_per_sample (int): Desired new bit depth (e.g., 16).

    Example:
    change_audio_quality("one.wav", "16bit.wav", 16)
    """
    os.system(f'sox -b {bits_per_sample} {input_file} {output_file}')

def convert_audio_channels(input_file, output_file, num_channels):
    """
    Convert the number of audio channels (e.g., mono to stereo or vice versa).

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output audio file with the desired number of channels.
    - num_channels (int): Number of channels (1 for mono, 2 for stereo).

    Example:
    convert_audio_channels("one.wav", "stereo.wav", 2)
    """
    os.system(f'sox {input_file} -c {num_channels} {output_file}')

def change_audio_speed(input_file, output_file, speed_factor):
    """
    Change the speed of an audio file.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output audio file with the changed speed.
    - speed_factor (float): Desired speed factor (e.g., 2.0 for doubling speed).

    Example:
    change_audio_speed("one.wav", "2x.wav", 2.0)
    """
    os.system(f'sox {input_file} {output_file} speed {speed_factor}')
