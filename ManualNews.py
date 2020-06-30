#!/usr/bin/python3
#sudo apt-get install python3-pil python3-pil.imagetk
from tkinter import *
import pyautogui
import subprocess
import time
import tkinter.font as tkFont
from PIL import ImageTk, Image
import webbrowser

#This function opens the image(screenshot)
def openimg():
    try:
        photo = Image.open('image.png')
        photo = photo.resize((1080, 720), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(photo)
        label = Label(Window, image=img)
        label.image = img
        label.grid(column=3,row=2)
    #This part catches the error if the image does not exist
    except:
        label1 = Label(text="The image you are trying to open does not exist", fg='red', font=fontStyle)
        label1.grid(column=1,row=1)

#This functions let's us to search in youtube
def youtube():
    ytsearch = Entry1.get()
    url2 = "https://www.youtube.com/results?search_query="+ytsearch
    webbrowser.open(url2)
    time.sleep(30)
    pyautogui.screenshot("image.png")
    subprocess.run("pkill firefox", shell=True, capture_output=True)

#This function removes the image from the folder
def removeimg():
    subprocess.run(" rm -f *.png", shell=True, capture_output=True)

#This entire code section is the GUI
Window = Tk()

#scrot must be installed on linux to use screenshot functions, run sudo apt-get install scrot
#This part is what let's us search in google
def search():
    #Manual search option
    search = Entry1.get()
    
    #Automatic search option
    #search = ""
    
    url = 'https://www.google.com/search?client=ubuntu&channel=fs&q=' + search + "&ie=utf-8&oe=utf-8"
    webbrowser.open(url)
    time.sleep(10)
    pyautogui.screenshot("image.png")
    #You can use pkill but the problem with it is that if you were browsing the web, then all your tabs will get closed as well.
    #subprocess.run("pkill firefox", shell=True, capture_output=True)
    
    #instead of pkill we will be using wmctrl which can be installed with sudo apt install wmctrl, and xdotool which can be installed with sudo apt install xdotool
    subprocess.run('wmctrl -a firefox; xdotool key Ctrl+w', shell=True)
    fwindow = subprocess.run('xdotool getactivewindow', shell=True, capture_output=True, text=True)
    fwindow2 = fwindow.stdout
    subprocess.run('xdotool windowminimize '+fwindow2, shell = True)
    
    #Comment this line if you do not want the screenshot to be open automatically
    #openimg()
#This determines the font
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

#This is the text input box
Entry1 = Entry(Window, font=fontStyle, bg="white", fg="black")
Entry1.grid(column=0, row=1)

#Youtube search button
button4 = Button(text="Youtube Search", command=youtube, font=fontStyle)
button4.grid(column=1, row=0)

#Open the screenshot button
button1 = Button(text="Open the screenshot", command=openimg, font=fontStyle)
button1.grid(column=2, row=0)

#Remove the image button
button2 = Button(text="Remove the image", command=removeimg, font=fontStyle)
button2.grid(column=3, row=0)

#Search button
button3 = Button(text="Search", command=search, font=fontStyle)
button3.grid(column=0, row=0)
                 
#Makes sure that the tkinter window opened is maximized
w, h = Window.winfo_screenwidth(), Window.winfo_screenheight()
Window.geometry("%dx%d+0+0" % (w, h))

#Determines the title name of the window
Window.title("AutoNews")

Window.mainloop()

#This makes sure that all the images are removed when the GUI is closed so the next time it is opened it doesn't cause conflict
removeimg()
