from utils.config import pygame
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
import os


currently_loaded_song = None
is_playing = False
progress = 0.0
current_time = None
max_time = None

def playSong(path):
    print(path)
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

def pathToFileType(path):
    _, extension = os.path.splitext(path)
    extension = extension.decode('utf-8')  # Decode bytes to string

    if ".mp3" in extension:
        return "mp3"
    elif '.flac' in extension:
        print("EXTENSION2")
        return "flac"
    else: 
        return "UNSUPORTED"

def getSongProgress():
    global progress
    if pygame.mixer.music.get_busy():
        song = None
        fileType = pathToFileType(currently_loaded_song)
        if fileType == "mp3":
            song = MP3(currently_loaded_song)
        elif fileType == "flac":
            song = FLAC(currently_loaded_song)
        else:
            return 0
        
        songLength = song.info.length
        if is_playing:
            current_position = pygame.mixer.music.get_pos() / 1000
            progress = (current_position / songLength) * 100
            return progress
        else:
            return progress
    else:
        return progress
