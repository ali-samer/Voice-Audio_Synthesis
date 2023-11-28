import os

def convert_audio_format(input_file, output_file):
    """
    Convert audio from one file format to another using FFmpeg.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output audio file with the desired format.

    Example:
    convert_audio_format('input.mp3', 'output.ogg')
    """
    os.system(f'ffmpeg -i {input_file} {output_file}')

def extract_audio_from_video(video_file, audio_file):
    """
    Extract audio from a video file using FFmpeg.

    Parameters:
    - video_file (str): Path to the input video file.
    - audio_file (str): Path to the output audio file.

    Example:
    extract_audio_from_video('video.mp4', 'audio.mp3')
    """
    os.system(f'ffmpeg -i {video_file} -vn -ab 256 {audio_file}')

def merge_audio_and_video(video_file, audio_file, output_file):
    """
    Merge audio and video files using FFmpeg.

    Parameters:
    - video_file (str): Path to the input video file.
    - audio_file (str): Path to the input audio file.
    - output_file (str): Path to the output video file.

    Example:
    merge_audio_and_video('video.mp4', 'audio.mp3', 'output.mp4')
    """
    os.system(f'ffmpeg -i {video_file} -i {audio_file} -c:v copy -c:a aac -strict experimental {output_file}')

def add_cover_image_to_audio(image_file, audio_file, output_file):
    """
    Add a cover image to an audio file and create a video using FFmpeg.

    Parameters:
    - image_file (str): Path to the cover image file.
    - audio_file (str): Path to the input audio file.
    - output_file (str): Path to the output video file.

    Example:
    add_cover_image_to_audio('image.jpg', 'audio.mp3', 'output.mp4')
    """
    os.system(f'ffmpeg -loop 1 -i {image_file} -i {audio_file} -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest {output_file}')

def crop_audio(input_file, output_file, start_time, duration):
    """
    Crop an audio file using FFmpeg.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output audio file after cropping.
    - start_time (str): Start time in HH:MM:SS format (e.g., '00:01:30').
    - duration (int): Duration in seconds to keep in the cropped audio.

    Example:
    crop_audio('inputfile.mp3', 'outputfile.mp3', '00:01:30', 30)
    """
    os.system(f'ffmpeg -ss {start_time} -t {duration} -acodec copy -i {input_file} {output_file}')

# Example usages (uncomment as needed):
# convert_audio_format('input.mp3', 'output.ogg')
# extract_audio_from_video('video.mp4', 'audio.mp3')
# merge_audio_and_video('video.mp4', 'audio.mp3', 'output.mp4')
# add_cover_image_to_audio('image.jpg', 'audio.mp3', 'output.mp4')
# crop_audio('inputfile.mp3', 'outputfile.mp3', '00:01:30', 30)
