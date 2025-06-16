import pygame 
from pygame.locals import * # type: ignore
import sys
import time
import nivel_uno
import home
import pestaña_bitacora

def para_volver_a_menu():
    volver_a_menu = home.Pestaña_Inicial()
    
def level_one():
    primer_nivel = nivel_uno.NivelUno()
    
def pestaña_de_bitacora():
    pestañas_de_la_bitacora = pestaña_bitacora.Pestaña_Bitacora()
class Controles:
    
    def __init__(self):
        
        ancho = 1300
        alto = 650
        reloj = pygame.time.Clock()
        rojo = (190, 0, 0)
        
        
        pygame.init()
        
        boton_volver_a_menu = pygame.image.load("boton_volver_a_menu.png")
        boton_volver_a_menu = pygame.transform.scale(boton_volver_a_menu, (270, 82))
        
        boton_comenzar = pygame.image.load("boton comenzar.png")
        boton_comenzar = pygame.transform.scale(boton_comenzar, (307, 82))
        
        screen = pygame.display.set_mode((ancho, alto))
        fondo_ventana_controles = pygame.image.load("pestaña de controles.png")
        fondo_ventana_controles = pygame.transform.scale(fondo_ventana_controles, (ancho, alto))

    ### ÁREAS ###

        area_boton_volver_a_menu = pygame.Rect (648, 500, 270, 82)
        area_boton_comenzar = pygame.Rect (964, 500, 270, 82)
        
        
        while True:
            
            pos_x, pos_y = pygame.mouse.get_pos()
            posicion_mouse = pos_x, pos_y = pygame.mouse.get_pos()
            evento_mouse_bajo =  pygame.MOUSEBUTTONDOWN
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                if event.type == evento_mouse_bajo:
                    if area_boton_comenzar.collidepoint(posicion_mouse):
                        pestaña_de_bitacora()
                    if area_boton_volver_a_menu.collidepoint(posicion_mouse):
                        para_volver_a_menu()
                
            pygame.display.set_caption("controles del juego")
            screen.blit(fondo_ventana_controles, (0, 0))
            
            if area_boton_comenzar.collidepoint(posicion_mouse):
                rectangulo_boton = pygame.Surface((317, 92))
                rectangulo_boton.fill(rojo)
                screen.blit(rectangulo_boton, (959, 495))
                screen.blit(boton_comenzar, (964, 500))


            if area_boton_volver_a_menu.collidepoint(posicion_mouse):
                rectangulo_boton = pygame.Surface( (280, 92))
                rectangulo_boton.fill(rojo)
                screen.blit(rectangulo_boton, (643, 495))
                screen.blit(boton_volver_a_menu, (648, 500))
            
            
            
            pygame.display.update()
            reloj.tick(60)

if __name__ == "__main__":
    Controles()