class AudioFile:
    def __init__(self,  filename):
        if not filename.endswith(self._ext):
            raise Exception("Invalid file format")
        self._filename = filename
            
    def play(self):
        raise NotImplementedError("Not implemented")
            
class MP3File(AudioFile):
    _ext  ="mp3"
    def play(self):
        print("Playing {} as mp3".format(self._filename))     
        
class WavFile(AudioFile):
    _ext  ="wav"
    def play(self):
        print("Playing {} as wav".format(self._filename))
        
class OggFile(AudioFile):
    _ext  ="ogg"
    def play(self):
        print("Playing {} as ogg".format(self._filename))
    
