from pytube import YouTube
import os

yt = YouTube(str(input("Enter URL>> ")))
video = yt.streams.get_audio_only()
print("Your Dest. Leave blank for current path")
destination = str(input(">> ")) or '.'
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file,new_file)
print(yt.title + " Download succesfully")
