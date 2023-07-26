import os
from moviepy.editor import *
import glob

lista_mp4 = glob.glob('*.mp4')

for video in lista_mp4:
    print('Reading mp4 archive')
    print('-'*10)
    mp4 = VideoFileClip(os.path.join(video))

    novo_nome = input(f"Enter the new name for the MP3 file (without the .mp3 extension) for the {video}: ")

    nome_mp3 = novo_nome + '.mp3'

    print('converting for mp3')
    mp4.audio.write_audiofile(os.path.join(nome_mp3))
    print('-'*20)
    print(f'converted mp4 {video} para mp3 {nome_mp3}')
