import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x300")
win.configure(bg="#C1CDCD")

#Botton function
def short():
    url = entry1.get()
    msg = "Your Shortened URL: "
    s = msg  + pyshorteners.Shortener().tinyurl.short( url)
    
    entry2.insert(END,s)

frame_line = Frame(win, width=400, height=5, bg="#3D59AB")
frame_line.pack(fill="x")

#Label for entering user url
Label(win,text="Enter your URL",font="arial 24 bold",bg="#C1CDCD",fg="#1A1A1A").pack(fill="x")

#frame_line = Frame(win, width=400, height=5, bg="#566FC6")
#frame_line.pack(fill="x")

#Entry box
entry1 = Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)

#Button
Button(win,text="Click Here",font="times 14 bold",bg="#3D59AB",fg="white",command=short).pack()

#Entry
entry2 = Entry(win,font="impack 10 bold",bd=0,width=60,bg="#C1CDCD")
entry2.pack(pady=30,padx=20)
    
mainloop()
