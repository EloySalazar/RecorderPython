
import sounddevice as sd
import wavio as wv
from scipy.io.wavfile import write

freq = 44100

print("Duration:")
duration = input()
duration = int(duration)


recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=2)


sd.wait()

print("name of file: "+ "example.wav" )

name = input()

write(name, freq, recording)


wv.write(name, recording, freq, sampwidth=2)
