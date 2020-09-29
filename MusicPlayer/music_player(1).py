""" Python Music Player """
#Importing python modules
import pygame
import tkinter as tkr
#Creating window
player = tkr.Tk()
#Edit window
player.title("Music Player")
player.geometry("205x340")
#Get song
file = "Song.mp3"
#Action event
def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()
#Register buttons
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button1.pack(fill="x")
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)
button2.pack(fill="x")
#Song name
label1 = tkr.LabelFrame(player, text="Song Name")
label1.pack(fill="both", expand="yes")
contents1 = tkr.Label(label1, text=file)
contents1.pack()
#Activate
player.mainloop()
