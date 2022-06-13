#!/home/melao/Codes/YTMuiscDownloader/env/bin/python3.10

import os
import PySimpleGUI as sg
from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import *


def downloadVideo(stream):
    musicPath = sg.popup_get_folder("Onde quer baixar?")
    try:
        videoPath = stream.download(musicPath)
        music = AudioFileClip(videoPath)
        music.write_audiofile(videoPath.replace("mp4", "mp3"))
        os.remove(videoPath)
        sg.popup("Deu tudo certo!")
    except Exception as error:
        sg.popup("Deu ruim!")
        print(error)


def getVideo(url):
    try:
        streams = YouTube(url).streams
        print(streams)
        stream = streams.get_audio_only()
        response = sg.popup_yes_no(f"Tem certeza que é o vídeo {stream.title}")
        if response == "Yes":
            downloadVideo(stream=stream)
    except Exception as error:
        sg.popup(f"Algo não deu certo!\n{error}")
        print(error)


def getURL():
    url = sg.popup_get_text("Digite a URL")
    getVideo(url)


if __name__ == "__main__":
    getURL()
