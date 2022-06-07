from pydub import AudioSegment
from pydub.utils import make_chunks
import os

class Split():
    def process_audio(self, file_name):
        myaudio = AudioSegment.from_file(file_name,"wav")
        chunk_length_ms = 6000 # pydub calculates in millisec
        chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec
        for i, chunk in enumerate(chunks):
            #chunk_name =  file_name[:-4] + "_{0}.wav".format(i)
            chunk_name = './signup_voice/javeria/' + file_name[:-4] + "_{0}.wav".format(i)
            # print ("exporting", file_name)
            chunk.export(chunk_name, format="wav")