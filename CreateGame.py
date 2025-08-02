import turtle
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light pink")
turtle_screen.title("Catch Game")


skor = 0
skorGosterge = turtle.Turtle()
skorGosterge.hideturtle()
skorGosterge.penup()
skorGosterge.goto(0,260)
skorGosterge.write(f"Skor: {skor}" , align = "center", font=("Arial", 20, "bold"))


kurbaga = turtle.Turtle()
kurbaga.shape("turtle")
kurbaga.color("green")
kurbaga.shapesize(4)
kurbaga.penup()

sure = 10
sayac_turtle = turtle.Turtle()
sayac_turtle.hideturtle()
sayac_turtle.penup()
sayac_turtle.goto(0,230)

oyun_bitti = False

def skoru_arttir(x, y):
    global skor
    if not oyun_bitti:
        skor += 1
        skorGosterge.clear()
        skorGosterge.write(f"skor: {skor}", align = "center", font=("Arial", 20, "bold"))

def kurbagayi_hareket_ettir():
    if not oyun_bitti:
        x = random.randint(-200,200)
        y = random.randint(-150,150)
        kurbaga.goto(x,y)
        turtle_screen.ontimer(kurbagayi_hareket_ettir, 1000)

def geri_say(t):
    global oyun_bitti
    if t>=0:
        mins, secs = divmod(t, 60)
        zaman = '{:02d}:{:02d}'.format(mins, secs)
        sayac_turtle.clear()
        sayac_turtle.write(zaman, align ="center", font=("Arial", 20, "bold"))
        turtle_screen.ontimer(lambda: geri_say(t - 1), 1000)
    else:
        oyun_bitti = True
        kurbaga.hideturtle()
        sayac_turtle.clear()
        sayac_turtle.write("GAME OVER", align = "center", font=("Arial", 20, "bold"))

kurbaga.onclick(skoru_arttir)
kurbagayi_hareket_ettir()
geri_say(sure)



turtle.done()

