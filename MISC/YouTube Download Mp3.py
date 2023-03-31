import os
import re
from tkinter import *
from pytube import YouTube
from moviepy.editor import AudioFileClip

def download_audio():
    # get the URL from the entry widget
    url = url_entry.get()

    # create a YouTube object and get the audio stream
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # download the audio stream
    audio_stream.download()

    # create an AudioFileClip object from the downloaded file
    audio = AudioFileClip(audio_stream.default_filename)

    # clean up the video title for use in the output filename
    title = re.sub(r'[^\w\s-]', '', yt.title)
    title = re.sub(r'[-\s]+', '_', title)
    title = title[:100]

    # save the audio as an mp3 file
    output_filename = f"{title}.mp3"
    audio.write_audiofile(output_filename)

    # close the audio stream
    audio.close()

    # delete the downloaded file
    os.remove(audio_stream.default_filename)

def download_video():
    # get the URL from the entry widget
    url = url_entry.get()

    # create a YouTube object and get the video stream
    yt = YouTube(url)
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

    # download the video stream
    video_stream.download()

    # rename the file to include the video title
    video_title = yt.title
    file_extension = video_stream.mime_type.split("/")[-1]
    new_filename = f"{video_title}.{file_extension}"
    old_filename = video_stream.default_filename
    os.rename(old_filename, new_filename)

root = Tk()
root.title("YouTube Downloader")

# create the URL label and entry widget
url_label = Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = Entry(root, width=50)
url_entry.pack()

# create the download audio button
audio_button = Button(root, text="Download Audio", command=download_audio)
audio_button.pack()

# create the download video button
video_button = Button(root, text="Download Video", command=download_video)
video_button.pack()

root.mainloop()
