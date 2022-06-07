from typing_extensions import Self
from winsound import PlaySound
import pyaudio as audio
import wave

from requests import post

def postvoice (self,time):
    stream = audio.open(input_device_index=self.device_index,
    output_device_index=self.device_index,
    format=self.format,
    channels=self.channel,
    rate=self.rate,
    input=True,
    frames_per_buffer=self.chunk
    )
    print("Recording...")
    frames = []
    for i in range(0, Self.rate / self.chunk * time):
        data = stream.read(self.chunk)
        frames.append(data)
    stream.stop_stream()
    print( "Recording Complete")
    stream.close()
    audio.terminate()
    write_frames= open_audio(self.file, 'wb')
    write_frames.setnchannels(self.channel)
    write_frames.setsampwidth(audio.get_sample_size(self.format))
    write_frames.setframerate(self.rate)
    write_frames.writeframes(''.join(frames))
    write_frames.close()
    self.convert()

    result = postvoice(3)
    print(result)