import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
from pytube import YouTube

def downloadVideo(stream):
    musicPath = sg.popup_get_folder('Onde quer baixar?')
    try:
        videoPath = stream.download(musicPath)
        print(videoPath)
        os.rename(videoPath, videoPath.replace('mp4', 'mp3'))
        sg.popup('Deu tudo certo!')
    except:
        sg.popup('Deu ruim!')

def getVideo(url):
    try:
        stream = YouTube(url).streams.get_audio_only()
        sg.popup_yes_no(f"Tem certeza que é o vídeo {stream.title}")
        downloadVideo(stream = stream)
    except:
        sg.popup('Algo não deu certo!')

def getURL():
    url = sg.popup_get_text('Digite a URL')
    getVideo(url)

if __name__ == '__main__':
    getURL()