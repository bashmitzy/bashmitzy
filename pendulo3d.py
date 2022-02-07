# pendulo3d.py

import pygame
from math import pi, sin, cos, floor
import sys
from pygame.time import set_timer

height = 700
width = 700
EVENTO_TIMER =26  # ENTRE 24 Y 32 PARA EVENTOS DE USUARIO
largo=0.3       #largo del pendulo en metros
gravedad=9.81   #  gravedad de la Tierra

# Inicialización. Siempre en un programa con pygame
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendulo Sencillo sin friccion")

pygame.font.init()

# define tipos de letra para marcar errores y para mensajes normales
font_mensajes = pygame.font.SysFont('Bauhuas 93', 30)

# función para poner mensajes de texto
def Escribe_texto(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    win.blit(img,(x, y))


def Dibuja_Eje(x,y,radio,color):
     pygame.draw.circle(win, color, (x, y), radio)

def Dibuja_Colgante(x,y,x2,y2,color,radio):
    pygame.draw.line(win, (216, 233, 168), (x,y), (x2, y2))
    pygame.draw.circle(win, color, (x2, y2), radio)

def calculo_Nuevo_Angulo(t,largo):
#  angulo,x,y=calculo_Nuevo_Angulo(angulo,largo)
    w=(gravedad/largo)**0.5
    #print('omega ',w*t)
    angulo=cos(w*t)  #calculamos la representacion del angulo de -1 a +1
    angulo=pi/2*angulo # normalizamos a 90 grados

    #print('angulo normalizado a 90 grados',angulo)
    x=largo*sin(angulo)
    y=largo*cos(angulo)
    #print('x ',x,' y ',y)
    return x,y
    
def update(window,largo,t):
    window.fill((25, 26, 25))
    x,y=calculo_Nuevo_Angulo(t,largo)
    y=-y
    x2=x*largo*2000; y2=-y*largo*2000   # normalizamos con el largo del pendulo y un factor de amplificacion
    print('x ',x,' y',y,' t ',t)   #  x,y son la distancia en pixeles
        
    Dibuja_Eje(width/2,20,10,(216, 233, 168))
    Dibuja_Colgante(width/2,20,width/2+x2,20+y2,(125,125,255),15)

    Escribe_texto("Pendulo en movimiento ",font_mensajes,(255,255,255), 50  , 300)
    Escribe_texto("Largo del colgante=  30 cm ",font_mensajes,(255,255,255), 50  , 320)
    Escribe_texto("Tarea: Explicar el procedimiento ",font_mensajes,(255,255,255), 50  , 340)
    Escribe_texto("Para calcular la velocidad tangencial ",font_mensajes,(255,255,255), 50 , 360)
    Escribe_texto("Con la tabla de valores x,y,t de la posicion de la masa ",font_mensajes,(255,255,255),50 , 380)
    pygame.display.update()

def main():
    run = True; t=0;viejot=0
    set_timer(EVENTO_TIMER, 50) # evento cada 50 mS
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == EVENTO_TIMER:
                t+=0.005   #no coindice con el tiempo real
                #print('tiempo en segs',t)
        if t!=viejot:        
           #print('viejot ',viejot)
           angulo=update(win,largo,t)
           viejot=t
main()  