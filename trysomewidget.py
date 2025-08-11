from tkinter import *
from tkinter import BooleanVar

window = Tk()
window.title("Nezi's Window")
window.minsize(width =400, height=100)

L = Label(window, text="My Label")
L.config(bg="pink",fg="white")
L.pack()

def button_clicked():
    print("button clicked")
    print(E.get())
    print(T.get("1.0", "end"))

B=Button(window, text = "Button", command=button_clicked)
B.pack()

E = Entry(width=10)
E.pack()

T = Text(window, width=10, height=10)
T.pack()

def selectedScale(Value):
    print(Value)

S = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=selectedScale )
S.pack()

def selectedSpinbox():
    Value = SB.get()
    print(Value)

SB = Spinbox(window, from_=0, to=100, width=5,command=selectedSpinbox)
SB.pack()

def ControlCheckButton():
    print(checkState.get())

checkState = BooleanVar()
Cb= Checkbutton(window, text="Checkbutton", variable=checkState, command=ControlCheckButton)
Cb.pack()

def ControlRadioButton():
    print(checkRadioButton.get())

checkRadioButton= IntVar()
radioButton= Radiobutton(window, text="OptionOne",value=10, variable=checkRadioButton, command=ControlRadioButton)
radioButton2= Radiobutton(window, text="OptionTwo",value=20, variable=checkRadioButton, command=ControlRadioButton)
radioButton.pack()
radioButton2.pack()

def selectedListbox(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(window)
myList = ["nezi", "eren", "ayca", "bulut"]

for i in range(len(myList)):
    listbox.insert(i, myList[i])

listbox.pack()
listbox.bind("<<ListboxSelect>>", selectedListbox)

window.mainloop()
