
#IMPORTING LIBRARIES
from pygame import mixer #Song play,pause,anything
import tkinter as tk #for GUI
from tkinter import * #For labels and buttons
from time import sleep
from tkinter.filedialog import askopenfilename
import random
from PIL import ImageTk,Image
from tkinter import messagebox
import mutagen
from mutagen.mp3 import MP3

#INITIALIZING
mixer.init()  
master = tk.Tk()           
master.title('Ƥђαηtσмs Player')
master.config(cursor='trek')
master.geometry('780x380')
n=0.5
#Configuration
master.iconbitmap("Images\\icon.ico")

img1=Image.open("Images\\3.jpg")
img11=ImageTk.PhotoImage(img1)
img2 = Label(image=img11)

img3=Image.open("Images\\6.jpg")
img33=ImageTk.PhotoImage(img3)
img4 = Label(image=img33)

img5=Image.open("Images\\7.jpg")
img55=ImageTk.PhotoImage(img5)
img6 = Label(image=img55)

img2.place(x=0,y=0)
master.configure(bg="skyblue")
ltitle=Label(master, text='Song Name',bg='gold',bd=5, wraplength=200, font='ariel 20 bold')
ltitle.place(x = 300 , y = 25)
vol = 'VOL'
lvol=Label(master,width = 5,height=2, text=vol,bg='red',foreground = 'black',bd=5, font = 'ariel 17 bold')
lvol.place(x = 347 , y = 190)

################################
#MAKING FUNCTIONS

def play():
    mixer.music.play()
def pause():
    mixer.music.pause()
def stop():
    mixer.music.stop()
def resume():
    mixer.music.unpause()
def select():
    global songname
    mixer.music.stop()
    songname = askopenfilename() #K:/Music/ Kaer Morhen.mp3
    mixer.music.load(songname)   #song1 = ['K:/Music','Kaer Morehn.mp3]
    mixer.music.set_volume(n)
    song1 = songname.rsplit('/',1)[1] #song = ['KAER mORHEN','mp3']
    song = song1.rsplit('.',1)[0] #song = Kaer Morhen
    v = (int(n*100))
    vol = (v,'%') #50%
    ltitle.configure(text = song)
    lvol.config(text=vol)
def up():
    global n
    n = n + 0.05 #n = 0.5+0.05
    if n > 1: #n >100
        n = 1
    mixer.music.set_volume(n) 
    v = (int(n*100))
    vol = (v,'%')
    lvol.config(text=vol)
    
def down():
    global n
    n = n - 0.05
    if n < 0:
        n = 0
    mixer.music.set_volume(n) 
    v = (int(n*100))
    if v < 0:
        v = 0
    vol = (v,'%')
    lvol.config(text=vol)

def playlist_select():
    mixer.music.stop()
    song_select = askopenfilename()
    fil = open('playlist.txt' , 'a')
    songx =  '\n' + song_select
    fil.write(songx)
    fil.close()

def play_playlist(): #load button
    global s
    global songname
    fil = open('playlist.txt' , 'r')
    strx = fil.read()
    s = strx.split('\n')
    if s[0] == '':
        del(s[0])          
    songname = s[0]
    mixer.music.load(songname)
    song1 = songname.rsplit('/',1)[1]
    song = song1.rsplit('.')[0]
    v = (int(n*100))
    vol = (v,'%')
    ltitle.configure(text = song)
    lvol.config(text=vol)

def prev():
    global song
    global songname
    indexx = s.index(songname) #getting index of currently running song
    if indexx == 0: #to iterate playlist
        indexx  = len(s)
    mixer.music.stop()
    prev_song_index = ((indexx)-1)
    songname = s[prev_song_index] #assigning new song address to variable songname
    mixer.music.load(songname) 
    mixer.music.set_volume(n)
    song1 = songname.rsplit('/',1)[1]
    song = song1.rsplit('.')[0]
    v = (int(n*100))
    ltitle.configure(text = song)
    mixer.music.play()
def nextz():
    global song
    global songname
    indexx = s.index(songname)
    if indexx == len(s)-1: 
        indexx  = -1
    mixer.music.stop()
    next_song_index = (indexx+1)
    songname = s[next_song_index]
    mixer.music.load(songname) 
    mixer.music.set_volume(n)
    song1 = songname.rsplit('/',1)[1]
    song = song1.rsplit('.')[0]
    v = (int(n*100))
    ltitle.configure(text = song)
    mixer.music.play()

def nonez():
    x = 'Hello G'

def autoplay():
    butresume.configure(command = nonez) #Disabling all other buttons to let program work correctly during autoplay
    butpause.configure(command = nonez)  #only volume button is available
    butplay.configure(command = nonez)
    butstop.configure(command = nonez)
    butselect.configure(command = nonez)
    butprev.configure(command = nonez)
    butnext.configure(command = nonez)
    butplayselect.configure(command = nonez)
    butplaylistplay.configure(command = nonez)
    butap.configure(command = nonez)
    play_playlist() #autoplay fucntion first loads the musix on the playlist
    autoplay_next() #then autplay calls this function to start songs on the playlist for autoplay
    

def autoplay_next(): #this function keeps calling itself again and again when a song stops and play next song automatically
    global song                                ########
    global songname                                   #
    indexx = s.index(songname)                        ##
    if indexx == len(s)-1:                            ###
        indexx  = -1                                  ####
    next_song_index = (indexx+1)                      ##### This is just
    songname = s[next_song_index]                     ##### copy of nextz
    mixer.music.load(songname)                        ##### button
    mixer.music.set_volume(n)                         ####
    song1 = songname.rsplit('/',1)[1]                 ###
    song = song1.rsplit('.')[0]                       ##
    v = (int(n*100))                                  #
    ltitle.configure(text = song)                     #
                                               ########
    mixer.music.play()
    song = MP3(songname) #to make it clear that song is MP3
    songlength = song.info.length #syntax to find length of song in sec
    songl = int(songlength)#converting length of song into integers
    length = songl*1000 #master.after asks miliseconds so making sec
    master.after(length+1000,autoplay_next) #1000 means adding one second more
   #master.after(time[mili second], function)
   #master.after adds an event to be run after time[miliseconds]
   #and it will be equal to length of song

modex  = 0
def darkmode():
    global modex
    if modex == 0:
        modex = 1
        butresume.config(bg = 'mediumblue',foreground = 'black')
        butpause.config(bg = 'dodgerblue',foreground = 'black')
        butplay.config(bg = 'fuchsia',foreground = 'black')
        butstop.config(bg = 'springgreen',foreground = 'black')
        butselect.config(bg = 'salmon',foreground = 'black')
        butup.config(bg = 'midnightblue',foreground = 'black')
        butdown.config(bg = 'aqua',foreground = 'black')
        butprev.config(bg = 'darkviolet',foreground = 'black')
        butnext.config(bg = 'green',foreground = 'black')
        butplayselect.config(bg = 'gold',foreground = 'black')
        butplaylistplay.config(bg = 'gold',foreground = 'black')
        butap.config(bg = 'yellow',foreground = 'black')
        img4.place(x=0,y=0)
        ltitle.config(bg = 'steelblue',foreground = 'black')
        lp.config(bg = 'tomato',foreground = 'black')
        lpp.config(bg = 'goldenrod',foreground = 'black')
        butst.config( bg = 'tomato',foreground = 'black')
        butmode.config(bg = 'orange',foreground = 'black')
        lvol.config(bg = 'red', foreground = 'black')


    elif modex  == 1:
        modex  = 2
        butresume.config(bg = 'black',foreground='blue')
        butpause.config(bg = 'black',foreground='blue')
        butplay.config(bg = 'black',foreground='blue')
        butstop.config(bg = 'black',foreground='blue')
        butselect.config(bg = 'black',foreground='cyan')
        butup.config(bg = 'black',foreground='lime')
        butdown.config(bg = 'black',foreground='lime')
        butprev.config(bg = 'black',foreground='yellow')
        butnext.config(bg = 'black',foreground='yellow')
        butplayselect.config(bg = 'black',foreground='deeppink')
        butplaylistplay.config(bg = 'black',foreground='deeppink')
        butap.config(bg = 'black',foreground='green')
        img6.place(x=0,y=0)
        ltitle.config(bg = 'black',foreground='white')
        lp.config(bg = 'black',foreground='cyan')
        lpp.config(bg = 'black',foreground='crimson')
        butst.config(bg = 'black',foreground='aqua')
        butmode.config(bg = 'black',foreground='springgreen')
        lvol.config(bg = 'black', foreground = 'orange')

    elif modex == 2:
        modex = 0
        butresume.config(bg = 'deepskyblue',foreground = 'black')
        butpause.config(bg = 'deepskyblue',foreground = 'black')
        butplay.config(bg = 'cyan',foreground = 'black')
        butstop.config(bg = 'cyan',foreground = 'black')
        butselect.config(bg = 'hotpink',foreground = 'black')
        butup.config(bg = 'lawngreen',foreground = 'black')
        butdown.config(bg = 'lawngreen',foreground = 'black')
        butprev.config(bg = 'darkgray',foreground = 'black')
        butnext.config(bg = 'darkgray',foreground = 'black')
        butplayselect.config(bg = 'cornflowerblue',foreground = 'black')
        butplaylistplay.config(bg = 'cornflowerblue',foreground = 'black')
        butap.config(bg = 'lightgreen',foreground = 'black')
        img2.place(x=0,y=0)
        ltitle.config(bg = 'gold',foreground = 'black')
        lp.config(bg = 'crimson',foreground = 'black')
        lpp.config(bg = 'royalblue',foreground = 'black')
        butst.config(bg = 'crimson',foreground = 'black')
        butmode.config(bg = 'orange',foreground = 'black')
        lvol.config(bg = 'red', foreground = 'black')


#################################
#MAKING AND PLACING RGB LABELS

l1=Label(master,bg='darkblue',height = 26,width=1)
l1.place(x = 0 , y = 0) 
l2=Label(master,bg='red',height = 26,width=1)
l2.place(x = 767 , y = 0) 
l3=Label(master,bg='limegreen',height = 1,width=110)
l3.place(x = 0 , y = 365) 
l4=Label(master,bg='yellow',height = 1,width=110)
l4.place(x = 0 , y = 0)

#################################
#MAKING BUTTONS

colors = ['lime','deeppink','yellow','red','blue']

frame = Frame(master)
frame.config(highlightbackground='blue',highlightthickness=10)

butresume = tk.Button(frame,text= u"\u23ef", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='deepskyblue',font='calibri', bd ='6', command = resume) 
butpause = tk.Button(frame, text= u"\u23f8", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='deepskyblue',font='calibri', bd ='6', command = pause) 
butplay = tk.Button(frame, text= u"\u23f5", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cyan',font='calibri', bd ='6', command = play) 
butstop = tk.Button(frame, text= u"\u23f9", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cyan',font='calibri', bd ='6', command = stop) 
butselect = tk.Button(master, text= 'Select', width=5,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='hotpink',font='calibri', bd ='6', command = select) 
butup = tk.Button(master, text=u'\u25B2', width=15,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='lawngreen',font='calibri', bd ='6', command = up) 
butdown = tk.Button(master, text=u'\u25BC', width=15,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='lawngreen',font='calibri', bd ='6', command = down) 
butprev = tk.Button(master, text= u"\u23ee", width=7,height=2,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='darkgray',font='calibri', bd ='6', command = prev) 
butnext = tk.Button(master, text= u"\u23ed", width=7,height=2,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='darkgray',font='calibri', bd ='6', command = nextz) 
butplayselect = tk.Button(master, text= "select", width=5,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cornflowerblue',font='calibri', bd ='6', command = playlist_select) 
butplaylistplay = tk.Button(master, text= "Load", width=5,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cornflowerblue',font='calibri', bd ='6', command = play_playlist) 
butap = tk.Button(master, text= 'AutoPlay', width=7,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='lightgreen',font='calibri', bd ='5', command = autoplay) 
butmode = tk.Button(master, text= 'Mode', width=7,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='orange',font='calibri', bd ='5', command = darkmode) 

#################################
#MAKING LABELS

lp = Label(master,text = 'Song', bg = 'crimson', height =1 ,width =10,font = 40)
lp.place(x=15, y=24)
lpp = Label(master,text = 'PlayList', bg = 'royalblue', height =1 ,width =9,font = 40)
lpp.place(x=648, y=24)

########################################
#PLACING BUTTONS

butplayselect.place(x=695, y=58)
butplaylistplay.place(x = 695, y = 108)
butselect.place(x=15, y=58)
butprev.place(x=82, y=182)
butnext.place(x=607, y=182)
butup.place(x =175, y = 200)
butdown.place(x = 432, y =200)
butap.place(x=675,y=313)
butmode.place(x = 15, y =315)

frame.place(x=142, y=270)

butplay.pack(side = LEFT)
butresume.pack(side = LEFT)
butpause.pack(side = LEFT)
butstop.pack(side = LEFT)

############################
#Easter Egg
def st():
    tk.messagebox.showinfo( "Important Notice", 'Special Thanks to Shahzeb @Electroboi')
butst = tk.Button(master, width=4,height=1,bg='crimson',bd=0,activebackground='crimson', command = st) 
butst.place(x=16,y=30)
master.resizable(0,0)
#RUNNING RGB AND MAINLOOP
# MAKING RGB

flag = True
def rgb(r, g, b):
    global flag
    sleep(0.005)
    waittime = 0
    master.update()
    l1.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    l2.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    l3.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    l4.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    frame.configure(highlightbackground=f"#{r:02x}{g:02x}{b:02x}")
    if flag:
        if (r != 255):
            master.after(waittime, rgb, r+1, g, b)
        elif (g != 255):
            master.after(waittime, rgb, r, g+1, b)
        elif (b != 255):
            master.after(waittime, rgb, r, g, b+1)
        else:
            flag = False
            master.after(waittime, rgb, r, g, b)
    if not flag:
        if (r != 0):
            master.after(waittime, rgb, r-1, g, b)
        elif (g != 0):
            master.after(waittime, rgb, r, g-1, b)
        elif (b != 0):
            master.after(waittime, rgb, r, g, b-1)
        else:
            flag = True
            master.after(waittime, rgb, r, g, b)
rgb(0,0,0)
master.mainloop()




