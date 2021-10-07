import os
from pytube import YouTube
from moviepy.editor import *

def downloadVideo(stream):
    musicPath = input('Onde quer baixar?\n')
    try:
        videoPath = stream.download(musicPath)
        video = VideoFileClip(videoPath)
        video.audio.write_audiofile(videoPath.replace('mp4', 'mp3'))
        os.remove(videoPath)
        print('Feito')
    except:
        print(':/')

def getVideo():
    url = input('Qual o link?')
    try:
        stream = YouTube(url = url).streams.get_lowest_resolution()
        escolha = input(f"Tem certeza que é esse link?\nTítulo: {stream.title}\n(S,N)")
    except:
        print('Deu bom não')
        return
    if escolha in ('sim', 's', 'Sim', 'S'):
        downloadVideo(stream)
    else:
        return

if __name__ == '__main__':
    getVideo()