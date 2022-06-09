from pathlib import Path

file_name = 'mubashir.wav'
Path('./signup_voice/'+file_name[:-4]).mkdir(parents=True, exist_ok=True)