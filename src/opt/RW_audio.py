from pydub import AudioSegment as aseg

def rw_audio(filepath: str):
    data = aseg.from_wav(filepath)
    data.export("new" + filepath)