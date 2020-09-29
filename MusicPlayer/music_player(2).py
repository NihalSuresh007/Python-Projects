""" Python Music Player """
#Importing python modules
import pygame
import tkinter as tkr
import os
#Creating window
player = tkr.Tk()
#Edit window
player.title("Music Player")
player.geometry("205x340")
#Playlist register
os.chdir("F:\Casual Projects\Music Player\Song")
print(os.getcwd)
songlist = os.listdir()
#Playlist input
playlist = tkr.Listbox(player, highlightcolor="blue", selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1
#Pygame inits
pygame.init()
pygame.mixer.init()
#Action event
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()
#Register buttons
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)

#Create song_name
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)
#Place widgets
button1.pack(fill="x")
button2.pack(fill="x")
songtitle.pack()
playlist.pack(fill="both", expand="yes")
#Activate
player.mainloop()
