from utils.config import pygame
from mutagen.mp3 import MP3


currently_loaded_song = None
is_playing = False

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

def getSongProgress():
    if pygame.mixer.music.get_busy():
        song = MP3(currently_loaded_song)
        songLength = song.info.length
        current_position = pygame.mixer.music.get_pos() / 1000
        progress = (current_position / songLength) * 100
        return progress
    else:
        return 0
