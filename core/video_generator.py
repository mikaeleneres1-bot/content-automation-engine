import subprocess
import os

os.makedirs("../output/video", exist_ok=True)

audio_files = sorted(os.listdir("../output/audio"))

if not audio_files:
    raise Exception("Nenhum áudio encontrado")

audio = audio_files[-1]

cmd = [
"ffmpeg",
"-loop","1",
"-i","../assets/background.jpg",
"-i",f"../output/audio/{audio}",
"-c:v","libx264",
"-c:a","aac",
"-shortest",
f"../output/video/{audio}.mp4"
]

subprocess.run(cmd)
