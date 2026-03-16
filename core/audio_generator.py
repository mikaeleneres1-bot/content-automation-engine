import os
import datetime
from gtts import gTTS
from script_generator import generate_script

# cria pasta de audio se não existir
os.makedirs("../output/audio", exist_ok=True)

script = generate_script()

timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M")

file_path = f"../output/audio/audio_{timestamp}.mp3"

tts = gTTS(script, lang="pt")

tts.save(file_path)

print("Audio gerado:", file_path)
