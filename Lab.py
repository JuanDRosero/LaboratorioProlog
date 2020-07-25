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

def isIn(item,lista):
  return  item in lista

def realizarAzzets(laberinto):
  parejas=[]
  #Escribir el asset de inicio a 2
  parejas +=[["inicio",2]]
  for f in range(2,len(laberinto)-2,2):
    for c in range(1,len(laberinto[1]),2):
      if laberinto[f][c]!="X" and laberinto[f][c]!="0":
        #Revisa arriba
        if laberinto[f-1][c] !="X":
          if laberinto[f-2][c]!="X" and laberinto[f-2][c]!="0":
              if not isIn([laberinto[f-2][c],laberinto[f][c]],parejas):
                  parejas +=[[laberinto[f][c],laberinto[f-2][c]]]
        #Revisa abajo
        if laberinto[f+1][c] !="X":
          if laberinto[f+2][c]!="X" and laberinto[f+2][c]!="0":
            if  not isIn([[laberinto[f+2][c]],laberinto[f][c]],parejas): 
                parejas +=[[laberinto[f][c],laberinto[f+2][c]]]
        #Revisa derecha
        if laberinto[f][c+1] !="X":
          if laberinto[f][c+2]!="X" and laberinto[f][c+2]!="0":
             if not isIn([laberinto[f][c+2],laberinto[f][c]],parejas): 
              parejas +=[[laberinto[f][c],laberinto[f][c+2]]]
        #revisa izquierda
        if laberinto[f][c-1] !="X":
          if laberinto[f][c-2]!="X" and laberinto[f][c-2]!="0":
             if not isIn([laberinto[f][c-2],laberinto[f][c]],parejas): 
                 parejas +=[[laberinto[f][c],laberinto[f][c-2]]]

  for item in range(len(parejas)):
    prolog.assertz("conecta(%s,%s)" % (parejas[item][0],parejas[item][1]))

def camino():
  lista = []
  for resultado in prolog.query("camino([inicio], Sol)"):
    for j in resultado["Sol"]:
      lista += [j]
    break
  lista[-1] = "inicio"
  lista[0] = "fin"
  return lista

def convertirString(lista):
  for i in range(len(lista)):
    lista[i] = str(lista[i])
  return lista

wn= turtle.Screen()
wn.bgcolor("Black")
wn.title("Laberinto")
wn.setup(400,400)
p= Penwall()
p2= Penexplorer("Yellow")
p3=Penexplorer("Black")
p4= Penfood()
realizarAzzets(leerLaberinto())
cam = convertirString(camino())
iniciarlab(leerLaberinto(),p,p4) 
explorar(cam,leerLaberinto(),p2,p3)