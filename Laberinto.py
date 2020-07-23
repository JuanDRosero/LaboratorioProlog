from pyswip import Prolog
import turtle
import time
prolog = Prolog()
prolog.consult("E:/INGENIERIA DE SISTEMAS/Quinto Semestre/Modelos II/Laberinto/Laberinto.pl")

class Penwall(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("blue")
    self.penup()
    self.speed(10)
class Penfood(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("circle")
    self.pensize(1)
    self.color("gray")
    self.penup()
    self.speed(10)
class Penexplorer(turtle.Turtle):
  def __init__(self,color):
    turtle.Turtle.__init__(self)
    self.shape("circle")
    self.color(color)
    self.penup()
    self.speed(10)

def iniciarlab(lab,penwall,penfood):
  for fila in range(len(lab)):
    for column in range (len(lab[fila])):
      muro=lab[fila][column]
      screen_x=-130+(column*22)
      screen_y=140-(fila*22)
      if (muro=="X"):
        penwall.goto(screen_x,screen_y)
        penwall.stamp()
      else:  
        if(muro!="0"):
          penfood.goto(screen_x,screen_y)
          penfood.stamp()
def pintar(num,lab,penexp):
  for fila in range(len(lab)):
    for column in range (len(lab[fila])):
      muro=lab[fila][column]
      screen_x=-130+(column*22)
      screen_y=140-(fila*22)
      if (muro==num):
          penexp.goto(screen_x,screen_y)
          penexp.stamp()
       
def explorar(camino,lab,p,p2):
  camino.reverse()   
  for i in range(len(camino)):
    pintar(camino[i],lab,p)
    if i>0:
      pintar(camino[i-1],lab,p2)
    time.sleep(0.2)

def leerLaberinto():
  x = [line.split() for line in open("E:/INGENIERIA DE SISTEMAS/Quinto Semestre/Modelos II/Laberinto/laberinto.txt" , "r").readlines()]
  return x  
"""  
def convertir():
    for result in prolog.query("sol"):
        print([result])
"""
wn= turtle.Screen()
wn.bgcolor("Black")
wn.title("Laberinto")
wn.setup(400,400)
p= Penwall()
p2= Penexplorer("Yellow")
p3=Penexplorer("Black")
p4= Penfood()
cam = list(prolog.query("sol"))
##convertir()
print(cam)
#cam=["fin", "32", "33", "34", "28", "27", "26", "20", "14", "15", "21", "22", "16", "10", "4", "3", "2", "inicio"]
#iniciarlab(leerLaberinto(),p,p4) 
#explorar(cam,leerLaberinto(),p2,p3)
