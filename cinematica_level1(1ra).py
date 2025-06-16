import pygame
from moviepy import VideoFileClip

pygame.init()
screen = pygame.display.set_mode((640, 360))
clip = VideoFileClip("video.mp4")  # Carga el video

clock = pygame.time.Clock()
running = True

for frame in clip.iter_frames():  # Itera sobre cada frame del video
    if not running:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Convierte el frame de NumPy a una superficie de Pygame
    frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    screen.blit(frame_surface, (0, 0))
    pygame.display.flip()
    clock.tick(clip.fps)  # Sincroniza con los FPS del video

clip.close()
pygame.quit()