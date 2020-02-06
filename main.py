# import pyglet
import pyaudio
import wave
import speech_recognition as sr

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio() # Initialize

    stream = pa.open( # Create stream
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk) # Initial chunk of stream

    while data_stream: # If more stream left continue
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    
    stream.close()
    pa.terminate()

play_audio('./audio/sms-alert-1-daniel_simon.wav')

# file = pyglet.resource.media('audio/eventually.mp3')
# file.play()

# pyglet.app.run()