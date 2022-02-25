import email, base64, wave

message = open("email.txt", "rb").read().decode()

mail = email.message_from_string(message)

audio = mail.get_payload(0).get_payload(decode=True)

f = open("indian.wav", "wb")

f.write(audio)



w = wave.open('indian.wav', 'rb')

h = wave.open("result.wav", "wb")

print(w.getnchannels())
print(w.getsampwidth())
print(w.getframerate())
h.setnchannels(w.getnchannels())
h.setsampwidth(w.getsampwidth()//2)
h.setframerate(w.getframerate()*2)
frames = w.readframes(w.getnframes())
wave.big_endiana = 1
h.writeframes(frames)

h.close()

