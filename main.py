from tkinter import *
import wikipedia

screen=Tk()
screen.title("Wiki Search App")
screen.geometry("500x400")
frame=Frame(screen)
input=Entry(frame,width=50)
input.pack()
text=Text(screen,font=('ariel',10))
result=''

def search():
  global result
  result=input.get()
  summ=wikipedia.summary(result,sentences=5)
  text.insert(END,summ)

button=Button(frame,text="search",bg="green",command=search)
button.pack(side=RIGHT)
frame.pack(side=TOP)
text.pack()


