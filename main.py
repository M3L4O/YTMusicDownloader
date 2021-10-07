import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
from pytube import YouTube
from moviepy.editor import *

def downloadVideo(stream):
    musicPath = sg.popup_get_folder('Onde quer baixar?')
    try:
        videoPath = stream.download(musicPath)
        video = VideoFileClip(videoPath)
        video.audio.write_audiofile(videoPath.replace('mp4', 'mp3'))
        os.remove(videoPath)
        sg.popup('Deu tudo certo!')
    except:
        print(':/')

def getVideo(url):
    try:
        stream = YouTube(url).streams.get_lowest_resolution()
        sg.popup_yes_no(f"Tem certeza que é o vídeo {stream.title}")
        downloadVideo(stream = stream)
    except:
        sg.popup('Algo não deu certo!')
        return

def getURL():
    url = sg.popup_get_text('Digite a URL')
    getVideo(url)

if __name__ == '__main__':
    getURL()