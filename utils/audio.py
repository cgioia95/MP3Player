from utils.config import pygame

currently_loaded_song = None

def playSong(path):
    global is_playing, currently_loaded_song
    if currently_loaded_song != path:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        currently_loaded_song = path
    else:
        pygame.mixer.music.unpause()
        is_playing = True

def pauseSong():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

def togglePlay():
    global is_playing
    if is_playing:
        pauseSong()
    else:
        playSong(currently_loaded_song)
