import os, shutil

for f in os.listdir():
    if f.endswith('.bin'):
        shutil.move(f, f.replace('.bin', '.mp4'))
