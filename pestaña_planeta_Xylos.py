import pygame
from pygame.locals import *
import sys
import nivel_uno
import controles_usuario

ventana_ancho = 1300
ventana_alto = 650
rojo = (190, 0, 0)


def level_one():
    primer_nivel = nivel_uno.NivelUno()
    
class Planeta_Xylos:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode((ventana_ancho, ventana_alto))
        pygame.display.set_caption("bitácora de planeta Xylos")
        
        fondo_menu = pygame.image.load("planeta Xylos.png")
        fondo_menu = pygame.transform.scale(fondo_menu, (ventana_ancho, ventana_alto))
        ima_rect_fondo = fondo_menu.get_rect()
        ima_rect_fondo.topleft = (0, 0)
        
        linea_seleccion = pygame.Surface((240, 5))
        linea_seleccion.fill(rojo)
    # Áreas
        area_planeta_xylos =pygame.Rect (202, 180, 270 ,52)
        
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
                    level_one()
            pygame.display.update()
            clock.tick(60)  # 60 FPS
if __name__ == "__main__":
    Planeta_Xylos()