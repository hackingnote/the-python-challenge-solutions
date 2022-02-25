from PIL import Image
import wave

wavs = [wave.open('lake/lake%d.wav' % i) for i in range(1,26)]
result = Image.new('RGB', (300,300), 0)
num_frames = wavs[0].getnframes()
for i in range(len(wavs)): 
    byte = wavs[i].readframes(num_frames)
    img = Image.frombytes('RGB', (60, 60), byte)
    result.paste(img, (60 * (i % 5), 60 * (i // 5)))
result.save('level25.png')


