# 021 - Faça um programa em Python que abra e reproduza o audio de um arquivo mp3:

import pygame
pygame.init() #iniciar o pygame
pygame.mixer.music.load('nome.mp3') #carregar o video
pygame.mixer.music.play() #executar
pygame.event.wait()
