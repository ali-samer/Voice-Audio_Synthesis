import ffmpy


def convert_wav(input_filename):
    """
    Convert an audio file to a different format using FFmpeg.

    Parameters:
    - input_filename (str): Path to the input audio file (e.g., .mp3).

    Example:
    convert_audio('test.mp3')
    """
    # Check if the input file type is supported
    supported_formats = ['.mp3', '.m4a', '.ogg']
    if input_filename[-4:] not in supported_formats:
        print(f"Error: Unsupported input file format for {input_filename}.")
        return

    output_filename = input_filename[:-4] + '.wav'

    ff = ffmpy.FFmpeg(
        inputs={input_filename: None},
        outputs={output_filename: None}
    )

    ff.run()

# Example usage:
# convert_audio('test.mp3')
