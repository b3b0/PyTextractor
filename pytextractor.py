from Tkinter import *
import tkFileDialog
from PIL import Image
from pytesseract import image_to_string

class PyTextractor:
    def __init__(self, master):
        self.master = master
        master.title("PyTextractor")
        master.geometry("500x500")
        master.resizable(0, 0)
        self.greet_button = Button(master, text="Open Image", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        target = tkFileDialog.askopenfilename()
        textinimage = image_to_string(Image.open(target))
        T.insert(END, textinimage)

root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

my_gui = PyTextractor(root)

root.mainloop()

