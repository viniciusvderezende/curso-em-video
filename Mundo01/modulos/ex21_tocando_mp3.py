import pygame

pygame.init()
pygame.mixer.music.load('euprotesto.mp3')
pygame.mixer.music.play()
input('Pressione Enter para parar a música.')
pygame.mixer.music.stop()