from tkinter import *
from pytube import YouTube
from moviepy.editor import *

root = Tk()
root.geometry('500x400')
root.resizable(0, 0)
root.title("Youtube Video Downloader and MP3 Converter")
root.configure(bg='#f2eee3')

Label(root, text='Youtube Video Downloader', font='arial 20 bold', bg="#f2eee3",fg="red").pack()

link = StringVar()
Label(root, text='Paste the YouTube Link Here', font = 'arial 15 bold', bg="#f2eee3").place(x=110, y=60)
link_enter = Entry(root, width = 30, textvariable=link, font='arial 15').place(x=80, y=100)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams[1]
    video.download()
    Label(root, text='Downloaded', font='arial 15', bg="#f2eee3", fg="red").place(x=190, y= 195)
    return video.download()

download_mp4 = Button(root,
    text='Download',
    font='arial 15 bold',
    bg='pale violet red',
    padx=2,
    command=downloader,
    fg="blue").place(x=190, y = 190)


root.mainloop()
