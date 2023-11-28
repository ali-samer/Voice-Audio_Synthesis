from pydub import AudioSegment


def load_audio(file_path):
    """
    Load an audio file using PyDub.

    Parameters:
    - file_path (str): Path to the input audio file.

    Returns:
    - AudioSegment: Loaded audio segment.

    Example:
    song = load_audio("never_gonna_give_you_up.wav")
    """
    return AudioSegment.from_wav(file_path)


def slice_audio(audio_segment, start_ms, end_ms):
    """
    Slice an audio segment in milliseconds.

    Parameters:
    - audio_segment (AudioSegment): Input audio segment.
    - start_ms (int): Start time in milliseconds.
    - end_ms (int): End time in milliseconds.

    Returns:
    - AudioSegment: Sliced audio segment.

    Example:
    ten_seconds = 10 * 1000
    first_10_seconds = slice_audio(song, 0, ten_seconds)
    last_5_seconds = slice_audio(song, -5000, None)
    """
    return audio_segment[start_ms:end_ms]


def adjust_volume(audio_segment, gain_dB):
    """
    Adjust the volume of an audio segment.

    Parameters:
    - audio_segment (AudioSegment): Input audio segment.
    - gain_dB (int): Volume adjustment in decibels.

    Returns:
    - AudioSegment: Audio segment with adjusted volume.

    Example:
    beginning = adjust_volume(first_10_seconds, 6)
    end = adjust_volume(last_5_seconds, -3)
    """
    return audio_segment + gain_dB


def concatenate_audio(segments):
    """
    Concatenate multiple audio segments.

    Parameters:
    - segments (list of AudioSegment): List of audio segments to concatenate.

    Returns:
    - AudioSegment: Concatenated audio segment.

    Example:
    without_the_middle = concatenate_audio([beginning, end])
    """
    return sum(segments)


def crossfade_audio(start_segment, end_segment, crossfade_ms):
    """
    Crossfade between two audio segments.

    Parameters:
    - start_segment (AudioSegment): First audio segment.
    - end_segment (AudioSegment): Second audio segment.
    - crossfade_ms (int): Crossfade duration in milliseconds.

    Returns:
    - AudioSegment: Crossfaded audio segment.

    Example:
    with_style = crossfade_audio(beginning, end, 1500)
    """
    return start_segment.append(end_segment, crossfade=crossfade_ms)


def repeat_audio(audio_segment, n):
    """
    Repeat an audio segment multiple times.

    Parameters:
    - audio_segment (AudioSegment): Input audio segment.
    - n (int): Number of times to repeat the segment.

    Returns:
    - AudioSegment: Repeated audio segment.

    Example:
    do_it_over = repeat_audio(with_style, 2)
    """
    return audio_segment * n


def fade_in_out(audio_segment, fade_in_ms, fade_out_ms):
    """
    Apply fade-in and fade-out effects to an audio segment.

    Parameters:
    - audio_segment (AudioSegment): Input audio segment.
    - fade_in_ms (int): Fade-in duration in milliseconds.
    - fade_out_ms (int): Fade-out duration in milliseconds.

    Returns:
    - AudioSegment: Audio segment with fade-in and fade-out effects.

    Example:
    awesome = fade_in_out(do_it_over, 2000, 3000)
    """
    return audio_segment.fade_in(fade_in_ms).fade_out(fade_out_ms)


def export_as_mp3(audio_segment, output_path):
    """
    Export an audio segment as an MP3 file.

    Parameters:
    - audio_segment (AudioSegment): Input audio segment.
    - output_path (str): Path to the output MP3 file.

    Example:
    export_as_mp3(awesome, "mashup.mp3")
    """
    audio_segment.export(output_path, format="mp3")


# Example usage:
"""
song = load_audio("never_gonna_give_you_up.wav")
ten_seconds = 10 * 1000
first_10_seconds = slice_audio(song, 0, ten_seconds)
last_5_seconds = slice_audio(song, -5000, None)
beginning = adjust_volume(first_10_seconds, 6)
end = adjust_volume(last_5_seconds, -3)
without_the_middle = concatenate_audio([beginning, end])
with_style = crossfade_audio(beginning, end, 1500)
do_it_over = repeat_audio(with_style, 2)
awesome = fade_in_out(do_it_over, 2000, 3000)
export_as_mp3(awesome, "mashup.mp3")
"""
