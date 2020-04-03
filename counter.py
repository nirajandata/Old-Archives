from tkinter import *
# pip install pillow
from PIL import Image, ImageTk
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open(r"C:\Users\niraj\OneDrive\Desktop\ext\Ewary\ab.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
L = Label(root, text="No clicks yet.")
L.pack()
app = Window(root)
root.wm_title("Counter")
root.geometry("540x600")

#counting function  
# Don't blame me for the messy code :P !
root.counter = 0
def clicked():
    root.counter += 1
    L['text'] = str(root.counter)
    if root.counter > 80:
        hyper = Label(root, text="Ho gaya vai !")
        hyper.pack()

def resets():
	root.counter=0
	L['text'] = 'No clicks yet.'
b = Button(root, text="Click",width= command=clicked)

b.pack(fill=Y, side=LEFT)
r = Button(root, text="reset", command=resets)
r.pack(fill=Y, side=RIGHT)

root.mainloop()
