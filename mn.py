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
app = Window(root)
root.wm_title("Counter")
root.geometry("540x600")

#counting function :P  
# Don't blame me for the messy code !
root.counter = 0
def clicked():
    root.counter += 1
    L['text'] = str(root.counter)
    if root.counter > 110:
        hyper = tk.Label(root, text="1 time !")
        hyper.pack()
def resets():
	root.counter=0
	L['text'] = 'No clicks yet.'
b = Button(root, text="Click", command=clicked)
b.pack()
r = Button(root, text="reset", command=resets)
b.pack()
L = Label(root, text="No clicks yet.")
L.pack()
root.mainloop()