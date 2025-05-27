import pygame
pygame.init()

pygame.mixer.music.load('eu_protesto.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():  # Mantém o script rodando enquanto a música toca
    pygame.time.Clock().tick(10)  # Pequena espera para evitar uso excessivo de CPU