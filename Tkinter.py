import tkinter as tk

#window
pencere = tk.Tk()
pencere.title("nezi pencere")
pencere.minsize(width=450,height=450)

def click_button():
    user_input = E.get()
    print(user_input)

#label
L = tk.Label(pencere, text="This is Nezi's Label", font="Arial")
L.config(bg="pink", fg="white")
#L.pack()
L.place(x=0,y=0)

#button
B = tk.Button(pencere, text="Button 1", command=click_button)
#B.pack()
B.place(x=225-33, y=225-16.5)
B.update()
print(B.winfo_height())
print(B.winfo_width())

#entry
E = tk.Entry(width=20)
#E.pack()
E.place(x=225-82,y=225-11.5)
E.update()
print(E.winfo_width())
print(E.winfo_height())

pencere.mainloop()