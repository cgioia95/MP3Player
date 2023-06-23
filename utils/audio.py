from utils.config import pygame

def playSong(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()