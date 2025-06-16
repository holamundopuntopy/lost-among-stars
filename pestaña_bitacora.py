import pygame
from pygame.locals import *
import sys
import nivel_uno
import controles_usuario
import pestaña_planeta_Xylos
ventana_ancho = 1300
ventana_alto = 650
rojo = (190, 0, 0)

def level_one():
    primer_nivel = nivel_uno.NivelUno()

def planeta():
    ventana_planeta_xylos =  pestaña_planeta_Xylos.Planeta_Xylos()
    
class Pestaña_Bitacora:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode((ventana_ancho, ventana_alto))
        pygame.display.set_caption("bitacora de viajera")
        
        fondo_menu = pygame.image.load("pestaña bitacora de viaje.png")
        fondo_menu = pygame.transform.scale(fondo_menu, (ventana_ancho, ventana_alto))
        ima_rect_fondo = fondo_menu.get_rect()
        ima_rect_fondo.topleft = (0, 0)
        
        linea_seleccion = pygame.Surface((370, 5))
        linea_seleccion.fill(rojo)
    # Áreas
        area_planeta_xylos =pygame.Rect (208, 180, 370 ,52)
        
        while True:
            pos_x, pos_y = pygame.mouse.get_pos()
            posicion_mouse = pos_x, pos_y = pygame.mouse.get_pos()
            evento_mouse_bajo =  pygame.MOUSEBUTTONDOWN
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(fondo_menu, ima_rect_fondo)
            if area_planeta_xylos.collidepoint(posicion_mouse):
                screen.blit(linea_seleccion, (208 ,230))
                if event.type == evento_mouse_bajo:
                    planeta()
            pygame.display.update()
            clock.tick(60)  # 60 FPS
if __name__ == "__main__":
    Pestaña_Bitacora()