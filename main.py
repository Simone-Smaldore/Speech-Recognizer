import whisper
import time

model = whisper.load_model('base')
start = time.time()
result = model.transcribe('Audio_Test_Lungo.m4a')
# result = model.transcribe('Registrazione.m4a')
#print(result['text'])

with open("transcription.txt", 'w') as f:
    f.write(result['text'])
print(f"Impiegati {time.time() - start} secondi")