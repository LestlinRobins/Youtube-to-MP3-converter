from pytube import YouTube
import os
from tkinter import *

root = Tk()
link_var = StringVar()
def submit(m):
    global link,type
    link = link_var.get()
    type = m
    exten = ""
    mp4btn["state"] = DISABLED
    mp3btn["state"]= DISABLED
    try:
        yt=YouTube(link)
        if type=="MP3":
            video = yt.streams.filter(only_audio=True).first()
            exten=".mp3"
        else:
            video = yt.streams.get_highest_resolution()
            exten=".mp4"
        out_file = video.download(output_path="C:/Users/lestl/Downloads")
        base,ext = os.path.splitext(out_file)
        new_file = base+exten
        os.rename(out_file,new_file)
        dlabel.configure(text=yt.title+" has been downloaded successfully.")
    except:
        dlabel.configure(text="The given URL doesn't exist or the file already exists!")
        mp4btn["state"] = NORMAL
        mp3btn["state"]= NORMAL
    
def next():
    mp4btn["state"] =NORMAL
    mp3btn["state"] = NORMAL

root.configure(bg="#121212")   
root.geometry("1366x768")   
root.title("YouTube to MP3 Converter") 
titlelabel =  Label(text = "Download Youtube Videos",bg="#121212",fg="#e0e0e0",font=("Google Sans",15))
titlelabel.place(x=525,y=170)
label = Label(text = "Enter the link to download:",bg="#121212",fg="#e0e0e0",font=("Google Sans",12))
label.place(x=225,y=270)
dlabel =  Label(text = "",bg="#121212",fg="#e0e0e0",font=("Google Sans",12))
dlabel.place(x=225,y=400)
entry = Entry(root,bg= "#333333",fg="#e0e0e0",textvariable=link_var,font = ("Google Sans", 12),relief=FLAT,width=90)
entry.place(x=225, y=300)
mp4btn=Button(root,text = 'Download MP4', command = lambda m = "MP4":submit(m),bg="#333333",fg="white",relief=FLAT,activebackground="#333333",activeforeground="white",font=("Google Sans",10))
mp4btn.place(x=470,y=350)
mp3btn=Button(root,text = 'Download MP3', command = lambda m = "MP3":submit(m),bg="#333333",fg="white",relief=FLAT,activebackground="#333333",activeforeground="white",font=("Google Sans",10))
mp3btn.place(x=586,y=350)
nextbtn=Button(root,text = 'Download other', command = next,bg="#333333",fg="white",relief=FLAT,activebackground="#333333",activeforeground="white",font=("Google Sans",10))
nextbtn.place(x=700,y=350)
root.mainloop()

