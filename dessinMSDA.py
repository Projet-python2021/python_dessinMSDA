import turtle
tur = turtle.Turtle()
def cercle(r):
#OBJECTIF:dessiner un cercle
#METHODE:turte
#BESOIN:rayon r,turtle
#CONNUS:
#ENTREES: rayon
#SORTIES:
#RESULTATS: dessine un cercle de rayon r
#HYPOTHESE:    
    tur.circle(r)

def demi_cercle(r):
#OBJECTIF:dessiner un demi_cercle
#METHODE:turte
#BESOIN:rayon r,turtle
#CONNUS:
#ENTREES: rayon,angle
#SORTIES:
##RESULTATS: dessine un demi_cercle de rayon r
#HYPOTHESE: l'angle est egale à 180 degrés
    tur.circle(r,180)
    
def carre(c):
#OBJECTIF:dessiner un carre
#METHODE: forward,left
#BESOIN:coté du carre c,l'angle 
#CONNUS:
#ENTREES:coté,l'angle
#SORTIES:
#RESULTATS: dessine un carré
#HYPOTHESE: angle est égal à 90 degrés
    tur.forward(c)
    tur.left(90) 
    tur.forward(c)
    tur.left(90)
    tur.forward(c)
    tur.left(90)
    tur.forward(c)
    tur.left(90)
    
def triangle(c, coul):
#OBJECTIF:dessiner un triangle
#METHODE: forward,left
#BESOIN:coté c, couleur
#CONNUS:
#ENTREES:coté,l'angle
#SORTIES:
#RESULTATS: dessine un triangle
#HYPOTHESE: angle est égal à 120 degrés
    tur.color(coul)
    tur.forward(c) 
    tur.left(120) 
    tur.forward(c)
    tur.left(120)
    tur.forward(c)
    
def rectangle(Long,larg, coul1, coul2="black"):
#OBJECTIF:dessiner un rectanleangle
# METHODE: forward,left,methode turtle
# BESOIN:longueur,largeur, couleur1,couleur2
#CONNUS:
#ENTREES: long,larg
#SORTIES:
#RESULTATS: dessine un rectangle
#HYPOTHESE: angle est égal à 90 degrés
    tur.color(coul1, coul2)
    for i in range (2):
        tur.forward(Long)
        tur.left(90)
        tur.forward(larg)
        tur.left(90)
               
def ellipse(r,coul1,coul2):
#OBJECTIF:dessiner une ellipse
#METHODE: methode turtle
#BESOIN: rayon,couleur
#CONNUS:
#ENTREES: rayon r
#SORTIES:
#RESULTATS: dessine une ellipse
#HYPOTHESE: angle est égal à 90 degrés"""
    tur.width(5)
    tur.color("blue")
    for i in range(2):   
        tur.circle(r,90)
        tur.circle(r/2,90)  
             
def trapeze(L,l,h,angle,coul):
#OBJECTIF:dessiner un trapeze
#METHODE: methode turtle,forward, right
#BESOIN: longueur L,largeur l,hauteur h,angle
#CONNUS:
#ENTREES: L,l,h
#SORTIES:
#RESULTATS: dessine un trapeze
#HYPOTHESE: angle est égal à 90 degrés"""
    tur.forward(l)
    tur.right(90)
    tur.forward(h)
    tur.right(90)
    tur.forward(L)
    tur.home()
    tur.done()

def losange (L):
#OBJECTIF:dessiner un losange
#METHODE: methode turtle,forward, right
#BESOIN: longueur 
#CONNUS:
#ENTREES:L
#SORTIES:
#RESULTATS: dessine un  losange
#HYPOTHESE:  la tortue toune à gauche de 45 degré et à droite de 90 degrés"""
    tur.left(45)
    tur.forward(L)  
    tur.right(90)
    tur.forward(L)
    tur.right(90)
    tur.forward(L)
    tur.right(90)
    tur.forward(L)
    tur.right(90)
    tur.done()
    
def polygone(n, L):
#OBJECTIF:dessiner un polygone
#METHODE: methode turtle,forward, right
#BESOIN: n,L 
#CONNUS:
#ENTREES:n,L
#SORTIES:
#RESULTATS: dessine un polygone
#HYPOTHESE: angle=360/n"""
    angle = 360 / n
    tur.color("black")
    for i in range(n):
        tur.forward(L)
        tur.right(-angle)
