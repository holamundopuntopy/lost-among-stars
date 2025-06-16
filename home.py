import pygame
from pygame.locals import *
import sys
import nivel_uno
import controles_usuario
import pestaña_bitacora
import pestaña_planeta_Xylos


ventana_ancho = 1300
ventana_alto = 650
rojo = (190, 0, 0)


def pestaña_controles():
    ventana_controles = controles_usuario.Controles()
    
def pestaña_bitacora_viaje():
    ventana_bitacora = pestaña_bitacora.Pestaña_Bitacora()

class Pestaña_Inicial:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode((ventana_ancho, ventana_alto))
        pygame.display.set_caption("Menú Principal")
        
        pygame.mixer.music.load('mazmorra.mp3')
        pygame.mixer.music.play(-1, 0.0) 
        
        fondo_menu = pygame.image.load("menú, comenzar o controles.png")
        fondo_menu = pygame.transform.scale(fondo_menu, (ventana_ancho, ventana_alto))
        ima_rect_fondo = fondo_menu.get_rect()
        ima_rect_fondo.topleft = (0, 0)

        imagen_boton_comenzar = pygame.image.load ("boton comenzar de menu.png")
        imagen_boton_comenzar = pygame.transform.scale (imagen_boton_comenzar, (272, 60))
        
        imagen_boton_controles = pygame.image.load("boton controles de menu.png")
        imagen_boton_controles = pygame.transform.scale (imagen_boton_controles, (270, 60))
        
    #Áreas    
        area_boton_comenzar = pygame.Rect (389, 413, 272, 60)
        area_boton_controles = pygame.Rect (722, 413 ,272, 60)
        
        while True:
            pos_x, pos_y = pygame.mouse.get_pos()
            posicion_mouse = pos_x, pos_y = pygame.mouse.get_pos()
            evento_mouse_bajo =  pygame.MOUSEBUTTONDOWN
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
            screen.blit(fondo_menu, ima_rect_fondo)
            
            if area_boton_comenzar.collidepoint(posicion_mouse):
                rectangulo_boton = pygame.Surface((282, 70))
                rectangulo_boton.fill(rojo)
                screen.blit(rectangulo_boton, (384, 408))
                screen.blit(imagen_boton_comenzar, (389, 413))
                if event.type == evento_mouse_bajo:
                    # crear area para cada cartel
                    pestaña_bitacora_viaje()
            
            if area_boton_controles.collidepoint(posicion_mouse):
                rectangulo_boton = pygame.Surface((282, 70))
                rectangulo_boton.fill(rojo)
                screen.blit(rectangulo_boton, (718, 408))
                screen.blit(imagen_boton_controles, (724 ,413))
                if event.type == evento_mouse_bajo:
                    # crear area para cada cartel
                    pestaña_controles()
            
            pygame.display.update()
            clock.tick(60)  # 60 FPS

if __name__ == "__main__":
    Pestaña_Inicial()