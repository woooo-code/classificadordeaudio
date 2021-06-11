import ffmpeg
import wave


name = "sample-000001"

out, _ = (ffmpeg
    .input(name+'.mp3')
    .output('-', format='s16le', acodec='pcm_s16le', ac=1, ar='22k')
    .overwrite_output()
    .run(capture_stdout=True)
)

CHANNELS = 1
RATE = 22000
swidth = 2

wf = wave.open('./'+name+'.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
wf.setframerate(RATE)
wf.writeframes(out)
wf.close()