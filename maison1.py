# Programme Python pour dessiner une maison avec lemodule turtle
# Import du module dessinMSDA
import dessinMSDA as D
# Import du module turtle
import turtle

# Dessin du rectangle noir
D.tur.begin_fill()
D.rectangle(100, 20, "black", 'black')
D.tur.end_fill()

# Dessin du carree
D.carre(100)

D.tur.penup()
D.tur.setpos(-5, 100)
D.tur.pendown()

# Dessin du triangle
D.triangle(110, "black")

D.tur.penup()
D.tur.setpos(20, 0)
D.tur.setheading(0)
D.tur.pendown()

# Dessin de la porte
D.rectangle(20, 75, "black")

#dessin des petits carree pour la fenetre*

move = 60
for i in range(2):
    D.tur.penup()
    D.tur.setpos(75, move)
    D.tur.setheading(60)
    D.tur.setheading(0)
    D.tur.pendown()
    D.carre(15)

    D.tur.penup()
    D.tur.setpos(60, move)
    D.tur.setheading(60)
    D.tur.setheading(0)
    D.tur.pendown()
    D.carre(15)
    move = move - 15

D.tur.penup()
D.tur.setpos(80, 120)
D.tur.setheading(0)
D.tur.pendown()

# Dessin de la porte
D.tur.begin_fill()
D.rectangle(20, 40, "black", "white")
D.tur.end_fill()

D.tur.penup()
D.tur.setpos(15, 1)
D.tur.pendown()


#dessin marge
D.tur.begin_fill()
D.rectangle(30, 18, "black", 'white')
D.tur.end_fill()

turtle.done()
