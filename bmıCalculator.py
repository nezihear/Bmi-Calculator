from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=100, height=100)

def sonucu_al():
    print(E1.get(), E2.get())

label1 = Label(window, text="Enter your weight:")
label1.pack()
E1 = Entry(window)
E1.pack()

label2 = Label(window, text="Enter your height:")
label2.pack()
E2 = Entry(window)
E2.pack()

def calculate_bmi():
    weight = int(E1.get())
    height = int(E2.get())
    boy_metre_cevir = height / 100
    bmi = weight / boy_metre_cevir ** 2
    print(round(bmi, 2))

    if bmi <= 18.5:
        print("ideal kilonun altında")
    elif 18.5 < bmi < 24.9:
        print("ideal kilo")
    elif 25 < bmi < 29.9:
        print("ideal kilonun üstünde ")
    elif 30 < bmi < 39.9:
        print("obez")
    elif bmi > 40:
        print("morbid obez")

B = Button(window, text="Calculate", command = calculate_bmi)
B.pack()


window.mainloop()