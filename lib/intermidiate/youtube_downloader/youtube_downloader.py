from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://youtu.be/7uEt6GQhRzI"

yt = YouTube(url, on_progress_callback = on_progress)
print("Title", yt.title)
print("Views", yt.views)

ys = yt.streams.get_highest_resolution()
ys.download()