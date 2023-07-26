import os
from moviepy.editor import *
import glob

lista_mp4 = glob.glob('*.mp4')

for video in lista_mp4:
    print('Lendo arquivo mp4')
    print('-'*10)
    mp4 = VideoFileClip(os.path.join(video))

    # Ask the user for the desired MP3 file name
    novo_nome = input(f"Digite o novo nome para o arquivo MP3 (sem a extensão .mp3) do vídeo {video}: ")

    nome_mp3 = novo_nome + '.mp3'  # Use the user-provided name for the MP3 file

    print('Convertendo para mp3')
    http://mp4.audio.write_audiofile(os.path.join(nome_mp3))
    print('-'*20)
    print(f'Converteu mp4 {video} para mp3 {nome_mp3}')