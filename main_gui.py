from tkinter import *
from detector import  detect
from recognize import recog
from datasetCreator import datacreate
from trainer import train

root = Tk()
root.geometry('300x300')
root.title("Photo-detector")


Button(root, text='Start detection',width=20,bg='brown',fg='white', command = detect).pack()

Button(root, text='Start recognition',width=20,bg='brown',fg='white', command = recog).pack()

Button(root, text='Add facial data',width=20,bg='brown',fg='white', command = datacreate).pack()

Button(root, text='Start training',width=20,bg='brown',fg='white', command = train).pack()

mainloop()






