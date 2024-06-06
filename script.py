from pytube import YouTube
from sys import argv

link = argv[1]
ytube = YouTube(link)

print("title: ",ytube.title)
tube_download = ytube.streams.get_highest_resolution()
tube_download.download('C://Users//USER//Videos')