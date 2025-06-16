import pygame # type: ignore
from pygame.locals import * # type: ignore
import sys
import time
import ajustes
import time

# variables fijas

inicio = time.time()
        
        #pantalla
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 650
     
        
#colooress
rojo = (255, 0, 0)
negro = (0, 0, 0)
blanco = (225,225,225)
def ajustes_de_usuario():
    ventana_ajutes = ajustes.Ajustes()
    
class NivelUno:
    def __init__(self):
        
        pygame.init()

        #tipos de eventos para tiempo
        reloj = pygame.time.Clock()
        inicio_tiempo = pygame.time.get_ticks()

        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("tutorial pygame de crear ventana")


    #agregar música
        pygame.mixer.music.load('sonido ambiente inicio.mp3')
        pygame.mixer.music.play(-1, 0.0)
    
        
    #contar tiempo
        tiempo_actual = pygame.time.get_ticks()
        tiempo_jugado = (tiempo_actual - inicio_tiempo) // 1000
        
    
        
    #variables aparte
        casi_final = 0
        cambio_1_hecho = 0
        seleccion_de_objetos = 0
        pateo_piedra = 0
        contador_de_clicks_en_area = 0
        frame = 0
        seleccion_gusano_lista = 0
        dar_gusano_a_pajaro = 0
        
    #definir acciones de mouse
        pos_x, pos_y = pygame.mouse.get_pos()

        
        # Definir imágenes
    #lo q es fondo
        fondo = pygame.image.load('fondo.jpg')
        fondo = pygame.transform.scale(fondo, (1300, 460))
        
        piedra_de_fondo = pygame.image.load('piedra_de_fondo.png')
        piedra_de_fondo = pygame.transform.scale(piedra_de_fondo, (150, 230))
        
        rectangulo = pygame.draw.rect(screen, negro, (0, 450, 1300, 200) )
        
        imagen_ajustes = pygame.image.load ("ajustes.png")
        imagen_ajustes = pygame. transform.scale(imagen_ajustes,(50, 50))
        
    #textos y fuentes
        fuente = pygame.font.SysFont('Courier New', 15)
        texto = fuente.render('¿Dónde estoy?...', True, negro)
        texto_gusano = fuente.render('lombriz', True, blanco)
        pos_text_gusano = (1215, 330)
        
        
        #movimiento
    #personaje
    #estático
        mi_imagen = pygame.image.load('personaa.png')
        mi_imagen = pygame.transform.scale(mi_imagen, (90, 120))
        
    #estático volteado
        mi_imagen_vol = pygame.transform.flip(mi_imagen, True, False)
        
    #cuando pasen 15s (Aún no listo)
        imaaburrida = pygame.image.load("aburrida.png")
        imaaburrida = pygame.transform.scale(mi_imagen, (90, 120))
        
    #para correr
        imagen_moviendo1 = pygame.image.load('correr.png')
        imagen_moviendo1 = pygame.transform.scale(imagen_moviendo1, (100, 120))
        
    #correr del otro lado
        imagen_moviendo2 = pygame.transform.flip(imagen_moviendo1, True, False)
        
    #salto
        imagen_salto1 = pygame.image.load('salto.png')
        imagen_salto1 = pygame.transform.scale(imagen_salto1, (100, 120))

        imagen_despegue = pygame.image.load('despegue.png')
        imagen_despegue = pygame.transform.scale(imagen_despegue, (130, 120))
    #cuando cae
        imagen_caida = pygame.image.load('caida.png')
        imagen_caida = pygame.transform.scale(imagen_caida, (100, 120))

    #para lado izquierdo
    #despegue inverso
        imagen_despegue_inverso = pygame.transform.flip(imagen_despegue, True, False)
        
    #salto inverso
        imagen_salto_inverso = pygame.transform.flip(imagen_salto1, True, False)

    #caida inversa
        imagen_caida_inversa = pygame.transform.flip(imagen_caida, True, False)

    #patada
        imagen_patear = pygame.image.load('patear.png')
        imagen_patear = pygame.transform.scale(imagen_patear, (100, 120))

        #imágenes cuervo
        #vuelo común
    #estático
        imagen_cuervo = pygame.image.load('cuervo_estatico.png')
        imagen_cuervo = pygame.transform.scale(imagen_cuervo, (65, 80))
        
    #alas abiertas 
        imagen_cuervo_vuelo1 = pygame.image.load('vuelo_mov1.png')
        imagen_cuervo_vuelo1 = pygame.transform.scale(imagen_cuervo_vuelo1, (80, 95))
        
    #alas casi todas abiertas 
        imagen_cuervo_vuelo2 = pygame.image.load('vuelo_mov_2.png')
        imagen_cuervo_vuelo2 = pygame.transform.scale(imagen_cuervo_vuelo2, (80, 95))
        imagen_cuervo_vuelo2_vol = pygame.transform.flip(imagen_cuervo_vuelo2, True, False)
        
    #alas termino medio 
        imagen_cuervo_vuelo3 = pygame.image.load('vuelo_mov3.png')
        imagen_cuervo_vuelo3 = pygame.transform.scale(imagen_cuervo_vuelo3, (80, 95))
        
    #alas abajo 
        imagen_cuervo_vuelo4 = pygame.image.load('vuelo_mov_4.png')
        imagen_cuervo_vuelo4 = pygame.transform.scale(imagen_cuervo_vuelo4, (80, 95))
            
            #vuelo caida
    #alas abiertas
        imagen_caida_cuervo1 = pygame.transform.flip(imagen_cuervo_vuelo1, True, False)
        
    # alas termino medio
        imagen_caida_cuervo2 = pygame.transform.flip(imagen_cuervo_vuelo2, True, False)
        
    #alas abajo
        imagen_caida_cuervo3 = pygame.transform.flip(imagen_cuervo_vuelo3, True, False)
        
        #picoteo
    #alto
        imagen_picoteo_cuervo1 = pygame.image.load('picoteo_cuervo_1.png')
        imagen_picoteo_cuervo1 = pygame.transform.scale(imagen_picoteo_cuervo1, (80, 95))
        
    #agachado medio
        imagen_picoteo_cuervo2 = pygame.image.load('Super_Pollo_2.png')
        imagen_picoteo_cuervo2 = pygame.transform.scale(imagen_picoteo_cuervo2, (80, 95))
     
    #agachado bajo
        imagen_picoteo_cuervo3 = pygame.image.load('picoteo_cuervo_3.png')
        imagen_picoteo_cuervo3 = pygame.transform.scale(imagen_picoteo_cuervo3, (80, 95))

    #agachado abajo
        imagen_picoteo_cuervo4 = pygame.image.load('picoteo_cuervo_4.png')
        imagen_picoteo_cuervo4 = pygame.transform.scale(imagen_picoteo_cuervo4, (80, 95))
        
        
        #piedra especial
    #piedrita estática
        imagen_piedra = pygame.image.load('piedra_estatica.png')
        imagen_piedra = pygame.transform.scale(imagen_piedra, (80, 90))
        
    #levemente levantada   
        imagen_piedra1 = pygame.image.load('piedra_mov_1.png')
        imagen_piedra1 = pygame.transform.scale(imagen_piedra1, (80, 90))

    #levntada
        imagen_piedra2 = pygame.transform.flip(imagen_piedra, False, True)
        
    #levemente mas que levantada
        imagen_piedra3 = pygame.image.load('piedra_mov_3.png')
        imagen_piedra3 = pygame.transform.scale(imagen_piedra3, (80, 90))
        
    #boca abajo
        imagen_piedra4 = pygame.transform.flip(imagen_piedra2, False, True)
        
    #piedra 2da
        piedra_parte_de_fondo = pygame.image.load('imagen_piedra2.png')
        piedra_parte_de_fondo = pygame.transform.scale(piedra_parte_de_fondo, (80, 90))
        
    #piedra 3ra
        piedra_fondo_fondo = pygame.image.load('imagen_piedra_3.png')
        piedra_fondo_fondo = pygame.transform.scale(piedra_fondo_fondo, (94, 16))
        
        #gusano
        imagen_gusano = pygame.image.load("gusano.png")
        imagen_gusano = pygame.transform.scale(imagen_gusano, (25, 25))
        
        #globo de dialogo
        imagen_globo_de_dialogo = pygame.image.load("burbuja_dialogo.png")
        imagen_globo_de_dialogo_invertida = pygame.transform.flip(imagen_globo_de_dialogo, True, False)
        
        #para fondo Glitch
        fondo_final2 = pygame.image.load("fondo_final_2,8.jpg")
        fondo_final2 = pygame.transform.scale(fondo_final2, (1300,460))
        
        fondo_final3 = pygame.image.load("fondo_final_3,5,9,11.jpg")
        fondo_final3 = pygame.transform.scale(fondo_final3, (1300,460))
        
        fondo_final4 = pygame.image.load("fondo_final_4,10.jpg")
        fondo_final4 = pygame.transform.scale(fondo_final4, (1300,460))
        
        fondo_final6 = pygame.image.load("fondo_final_6,12.jpg")  
        fondo_final6 = pygame.transform.scale(fondo_final6, (1300,460))
        
        fondo_final13 = pygame.image.load("fondo_final_13.jpg")
        fondo_final13 = pygame.transform.scale(fondo_final13, (1300,460))
        
        fondo_final14 = pygame.image.load("fondo_final_14.jpg")
        fondo_final14 = pygame.transform.scale(fondo_final14, (1300,460))
        
        fondo_final15 = pygame.image.load("fondo_final_15.jpg")
        fondo_final15 = pygame.transform.scale(fondo_final15, (1300,460))
        
        fondo_final16 = pygame.image.load("fondo_final_16.png")
        fondo_final16 = pygame.transform.scale(fondo_final16, (1300,460))
        
        piedra_cascada = pygame.image.load("piedra_cascada.png")
        piedra_cascada = pygame.transform.scale(piedra_cascada, (105,376))
        
        #para interfaz de usuario
        cuadrado_blanco = pygame.Surface((40, 40))
        cuadrado_blanco.fill(blanco)
        
        
        
        
                                    # Para animación rápida
    #personaje
        animacion_derecha = [imagen_moviendo1, mi_imagen]
        animacion_izquierda = [imagen_moviendo2, mi_imagen_vol]
        animacion_salto_derecha = [imagen_caida, imagen_despegue, imagen_salto1, imagen_caida]
        animacion_salto_izquierda = [imagen_caida_inversa, imagen_despegue_inverso, imagen_salto_inverso, imagen_caida_inversa]
        animacion_patear = [mi_imagen, imagen_patear]
    
    #cuervo
        animacion_vuelo = [imagen_cuervo_vuelo1, imagen_cuervo_vuelo2_vol, imagen_cuervo_vuelo3, imagen_cuervo_vuelo4]
        animacion_bajada = [imagen_caida_cuervo1, imagen_cuervo_vuelo2, imagen_caida_cuervo2, imagen_caida_cuervo3]
        animacion_picoteo = [imagen_picoteo_cuervo1, imagen_picoteo_cuervo2, imagen_picoteo_cuervo3, imagen_picoteo_cuervo4]
    
    #piedra
        animacion_rotacion_piedra = [imagen_piedra, imagen_piedra2, imagen_piedra3, imagen_piedra4]
        
    #Glitch
        animacion_glitch_final = [fondo, fondo_final2, fondo_final3, fondo_final4, fondo_final3, fondo_final6, fondo, fondo_final2, fondo_final3,fondo_final4,fondo_final3, fondo_final6, fondo_final13, fondo_final14, fondo_final15]
        animacion_mini_glitch = [fondo_final16, fondo_final14, fondo_final15, fondo_final13]
        




                                    ############## EJES #############
        
        #para personaje
        ima_rect = mi_imagen.get_rect()
        ima_rect.center = (50, 340)

        #para el cuervo
        ima_rect_cuervo = imagen_cuervo.get_rect()
        ima_rect_cuervo.center = (360, int(SCREEN_HEIGHT / 2.4))
        
        #para piedra grande central cerca de cascada
        ima_rect_piedra = imagen_piedra.get_rect()
        ima_rect_piedra.center = (1240, 375)
        
        #para el gusano
        ima_rect_gusano = imagen_gusano.get_rect()
        ima_rect_gusano.center = (1233,375)
        
        # pos de gusano 3
        ima_rect_gusano2 = imagen_gusano.get_rect()
        ima_rect_gusano2.center = (650,390)
        
        #para el globo de texto
        ima_rect_globo = imagen_globo_de_dialogo_invertida.get_rect()
        ima_rect_globo.center = (150, 270)
        
        #para el texto dentro del globo
        rect_dialogo = texto.get_rect()
        rect_dialogo.center = (148, 259)
        
        #para el fondo Glitch
        ima_rect_fondo = fondo.get_rect()
        ima_rect_fondo.center = (650, 230)
        
        #para fondo final
        ima_rect_piedra_cascada = piedra_cascada.get_rect()
        ima_rect_piedra_cascada.center = (0,37)
        
        #interfaz de usuario
        ima_rect_piedra_fondo_en_si2 =  piedra_fondo_fondo.get_rect()
        ima_rect_piedra_fondo_en_si2 = (851, 399)


                            ######### ÁREAS ############
        area_permitida = pygame.Rect (0, 275, 1300, 187)
        area_cuervo = pygame.Rect (200, 0, 300, 600)
        area_piedra =  pygame.Rect (1200, 322, 150, 100)
        area_gusano = pygame.Rect (1200, 315, 100, 100)
        area_gusano2 = pygame.Rect (10, 10, 500, 650)# acomodaar lugar de área
        area_cuarado_blanco = pygame.Rect (5, 465, 40, 40)
        area_ajustes = pygame.Rect (1200, 0, 450 ,50)
        
    # mostrar fondo antes de jugar
        screen.blit(fondo, (0, 0))       
        screen.blit(imagen_gusano, ima_rect_gusano)
        screen.blit(imagen_piedra, ima_rect_piedra)
        screen.blit(mi_imagen, ima_rect)
        screen.blit(imagen_piedra,ima_rect_piedra)
        screen.blit(piedra_de_fondo, (300,250))  
        screen.blit(imagen_cuervo, ima_rect_cuervo)# Luego el personaje encima
        screen.blit(imagen_globo_de_dialogo_invertida, ima_rect_globo)
        screen.blit(texto, (rect_dialogo))
        screen.blit(imagen_ajustes, (1250, 0))
        pygame.display.update()
        pygame.time.delay(1000)
        


    ##################################### coso repetir principal ############################################    
    #########################################################################################################    

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            

            posicion_mouse = pos_x, pos_y = pygame.mouse.get_pos()
            evento_mouse_bajo =  pygame.MOUSEBUTTONDOWN
            evento_mouse_arriba =  pygame.MOUSEBUTTONUP
            tecla = pygame.key.get_pressed()
            imagen_actual = mi_imagen
            imagen_actual_cuervo = imagen_cuervo
            imagen_actual_piedra = imagen_piedra
            imagen_actual_fondo = fondo
            


    ###################################### animacion en mov con teclas ###########################################
    ##############################################################################################################  
           
            
        #ejecución mover derecha    
            if tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
                imagen_actual = animacion_derecha[frame % 2]
                ima_rect.x += 20
        
        #ejecución mover izquieda
            elif tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
                imagen_actual = animacion_izquierda[frame % 2]
                ima_rect.x -= 20
        
        #ejecución subir
            elif tecla[pygame.K_w] or tecla[pygame.K_UP]:
                imagen_actual = animacion_izquierda[frame % 2]
                ima_rect.y -= 20
        
        #ejecución bajar
            elif tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
                imagen_actual = animacion_izquierda[frame % 2]
                ima_rect.y += 20
        
        #ejecución correr
            if (tecla[pygame.K_LSHIFT] and (tecla[pygame.K_d] or tecla[pygame.K_RIGHT])):
                imagen_actual = animacion_derecha[frame % 2]
                ima_rect.x += 50
        
            if (tecla[pygame.K_LSHIFT] and (tecla[pygame.K_a] or tecla[pygame.K_LEFT])):
                imagen_actual = animacion_izquierda[frame % 2]
                ima_rect.x -= 50
                
        #ejecución salto
            if tecla[pygame.K_SPACE]:
                imagen_actual = animacion_salto_derecha[frame % 4]
                ima_rect.y -= 35
                ima_rect.y +=35

            if (tecla[pygame.K_SPACE] and (tecla[pygame.K_a] or tecla[pygame.K_LEFT])):
                imagen_actual = animacion_salto_izquierda[frame % 4]
                ima_rect.y -= 35
                ima_rect.x -= 35
                ima_rect.y +=35
            
            if (tecla[pygame.K_SPACE] and (tecla[pygame.K_d] or tecla[pygame.K_RIGHT])):
                imagen_actual = animacion_salto_derecha[frame % 4]
                ima_rect.y -= 35
                ima_rect.x += 35
                ima_rect.y +=35
                        
        #ejecucion patear
            elif tecla[pygame.K_f]:
                imagen_actual = animacion_patear[frame % 2]
                
            if tecla[pygame.K_t]:
                casi_final += 1
  
                
# no funciona        
#########################################################################################################
            if tecla[pygame.K_y]:
                imagen_actual = imaaburrida
                print(type(imaaburrida))  # Debe mostrar: <class 'pygame.Surface'>
                print(type(imagen_actual))# para saber si carga la imagen
                pygame.display.update()
                pygame.time.delay(1000)
                
#########################################################################################################

    
    #interacción con objetos 


            if ima_rect.colliderect(area_cuervo):
                imagen_actual_cuervo = animacion_vuelo[frame % 4]
                ima_rect_cuervo.y -= 35
                
            if not ima_rect.colliderect(area_cuervo):
                if ima_rect_cuervo.y<226:
                    imagen_actual_cuervo = animacion_vuelo[frame % 4]
                    ima_rect_cuervo.y += 10
                else:
                    imagen_actual_cuervo = imagen_cuervo 
                     
            if pateo_piedra != 1:
                if ima_rect.colliderect(area_piedra) and tecla[pygame.K_f]:
                    imagen_actual_piedra = animacion_rotacion_piedra[frame % 4]
                    ima_rect_piedra.x += 50
                    pateo_piedra +=1


                                #Limitar el movimiento dentro del área
            ima_rect.clamp_ip(area_permitida)
            ima_rect_cuervo.clamp_ip(area_cuervo)
            ima_rect_piedra.clamp_ip(area_piedra)
            
            frame += 1

            
    ##################################### MOSTRAR EN PANTALLA ###############################################        # DIBUJAR
    ########################################################################################################        
            if casi_final != 1: # si no es igual al glitch
                screen.blit(fondo, (0, 0))                
                screen.blit(imagen_gusano, ima_rect_gusano)
                screen.blit(imagen_actual_piedra, ima_rect_piedra)
            
    #################################### cambio importante del juego ########################################################            
                if pateo_piedra == 1: # si se pateó piedra  
                    
                    if area_gusano.collidepoint(posicion_mouse):# si la pocicion del mouse ta en el area del coso
                        screen.blit(texto_gusano, pos_text_gusano)#  se muestra el texto lombriz arriba
                        
                        if event.type == evento_mouse_bajo:# si el tipo de evento q se hace es uno tipo mause
                            ima_rect_gusano = (5, 465) # se dibuja lombriz en cuadrado
                            screen.blit(cuadrado_blanco, (5, 465) )#mostrar
                            screen.blit(imagen_gusano,ima_rect_gusano)#mostrar
                            area_gusano = area_cuarado_blanco
                        
                    if area_cuarado_blanco.collidepoint(posicion_mouse):# si la pocicion del mouse ta en el area del coso
                        pos_text_gusano =(2, 445)
                        texto_gusano = fuente.render('lombriz', True, negro)
                        screen.blit(texto_gusano, pos_text_gusano)
                    
                    if area_cuervo.collidepoint(posicion_mouse):
                            if event.type == evento_mouse_bajo:
                                seleccion_gusano_lista = 1
                                dar_gusano_a_pajaro = 1
                                
                    if seleccion_gusano_lista == 1:
                        
                    
###################################### terminar #################################################################
##################################################################################################################
                                
                        if dar_gusano_a_pajaro == 1:
                            if ima_rect.y != 320:
                                if ima_rect.y < 320:
                                    imagen_actual = animacion_derecha [frame % 2]
                                    ima_rect.y += 20
                                if ima_rect.y > 320:
                                    imagen_actual = animacion_derecha [frame % 2]
                                    ima_rect.y -= 20
                            else:
                                imagen_actual = mi_imagen_vol
                                
                            if ima_rect.x != 765:
                                if ima_rect.x <= 765:
                                    imagen_actual = animacion_derecha [frame % 2]
                                    ima_rect.x += 20
                                if ima_rect.x >= 765:
                                    imagen_actual = animacion_izquierda [frame % 2]
                                    ima_rect.x -= 20
                            else:
                                imagen_actual = mi_imagen_vol
                                screen.blit(imagen_actual, ima_rect)
                                
########################### td piola pero luego deja de moverse #######################################################
#######################################################################################################################                        
                        if area_cuervo.collidepoint(posicion_mouse):
                            if event.type == evento_mouse_bajo:# si el tipo de evento q se hace es uno tipo mause
                                ima_rect_gusano = (750, 400)
                                pos_text_gusano =(2, 600)
                                screen.blit(cuadrado_blanco, (5, 465) )
                                screen.blit(imagen_gusano,ima_rect_gusano)
                                screen.blit(imagen_actual, ima_rect)
                    
###################################################################################################################
########################################################################################################################
                   
    # para agregarle sentido a las imagenes, no pasa x encima de la piedra raro          
                if area_ajustes.collidepoint(posicion_mouse):
                    if event.type == evento_mouse_bajo:
                        ajustes_de_usuario()
                
                if ima_rect.y>322:
                    screen.blit(imagen_actual, ima_rect)
                    screen.blit(imagen_actual_piedra,ima_rect_piedra)
                else:
                    screen.blit(imagen_actual_piedra,ima_rect_piedra)
                    screen.blit(imagen_actual, ima_rect)
                
                if ima_rect.y > 200:
                    screen.blit(imagen_actual, ima_rect)
                    screen.blit(piedra_fondo_fondo, ima_rect_piedra_fondo_en_si2)
                else:
                    screen.blit(piedra_fondo_fondo, ima_rect_piedra_fondo_en_si2)
                    screen.blit(imagen_actual, ima_rect)
                    
    # para cuando la mina pasa x la piedra del pájaro          
                if ima_rect.y<300:
                    screen.blit(imagen_actual, ima_rect)
                    screen.blit(piedra_de_fondo, (300,250))
                else:
                    screen.blit(piedra_de_fondo, (300,250))
                    screen.blit(imagen_actual, ima_rect)
                screen.blit(imagen_actual_cuervo, ima_rect_cuervo)# Luego el personaje encima    

                    
            
            else:
                imagen_actual_fondo = animacion_glitch_final[frame % 15]
                screen.blit(imagen_actual_fondo, ima_rect_fondo) #Glitch
                pygame.display.update()
                reloj.tick(30)
            
            screen.blit(imagen_ajustes, (1250, 0))
            pygame.display.flip()
            reloj.tick(15)

if __name__ == "__main__":
    NivelUno()