import pygame
from pygame.locals import *
import sys
import nivel_uno
import controles_usuario
import pestaña_planeta_Xylos
import home


ventana_ancho = 1300
ventana_alto = 650

#colores
black = (0, 0, 0, 90)
rojo = (225, 0, 0)


def level_one():
    primer_nivel = nivel_uno.NivelUno()

def volver_a_menu():
    para_volver_a_menu = home.Pestaña_Inicial()
    
class Ajustes:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode((ventana_ancho, ventana_alto))
        pygame.display.set_caption("bitacora de viajera")
        
        primer_fondo = pygame.image.load("fondo.jpg")
        primer_fondo = pygame.transform.scale(primer_fondo, (1300, 450))
        
        fondo_pausa = pygame.image.load("estado_de_pausa.png")
        fondo_pausa = pygame.transform.scale(fondo_pausa, (1000, 450))

        rectangulo_difuminado = pygame.Surface(((ventana_ancho, ventana_alto)), pygame.SRCALPHA)
        rectangulo_difuminado.fill(black)

        
    #Áreas
        area_boton_reiniciar = pygame.Rect (467, 167, 385, 65)
        area_boton_guardar = pygame.Rect (467, 245, 385, 65)
        area_boton_volver_a_menu = pygame.Rect (467, 345, 385, 65)
        
        while True:
            pos_x, pos_y = pygame.mouse.get_pos()
            posicion_mouse = pos_x, pos_y = pygame.mouse.get_pos()
            evento_mouse_bajo =  pygame.MOUSEBUTTONDOWN
            evento_mouse_arriba =  pygame.MOUSEBUTTONUP
            ajustes_1 = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            screen.blit(primer_fondo, (0, 0))
            
            if area_boton_guardar.collidepoint(posicion_mouse):
                rectangulo_seleccion = pygame.Surface((388, 68))
                rectangulo_seleccion.fill(rojo)
                screen.blit(rectangulo_seleccion, (467,258))
            # hacer base de datos
            
            if area_boton_volver_a_menu.collidepoint(posicion_mouse):
                rectangulo_seleccion = pygame.Surface((388, 68))
                rectangulo_seleccion.fill(rojo)
                screen.blit(rectangulo_seleccion, (467, 345))
                if event.type == evento_mouse_bajo:
                    volver_a_menu()
                
            if area_boton_reiniciar.collidepoint(posicion_mouse):
                rectangulo_seleccion = pygame.Surface((388, 68))
                rectangulo_seleccion.fill(rojo)
                screen.blit(rectangulo_seleccion, (467, 175))
                if event.type == evento_mouse_bajo:
                    level_one()
                    
            screen.blit(rectangulo_difuminado, (0 ,0))
            screen.blit(fondo_pausa, (160, 10))
            
                
            
            pygame.display.update()
            clock.tick(60)  # 60 FPS
if __name__ == "__main__":
    Ajustes()