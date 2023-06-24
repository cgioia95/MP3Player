from utils.config import pygame
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
import os


currently_loaded_song = None
is_playing = False

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

    print("EXTENSION")
    print(extension)
    if ".mp3" in extension:
        print("EXTENSION1")
        return "mp3"
    elif '.flac' in extension:
        print("EXTENSION2")
        return "flac"
    else: 
        return "UNSUPORTED"



def getSongProgress():
    if pygame.mixer.music.get_busy():
        song = None
        fileType = pathToFileType(currently_loaded_song)
        if (fileType == "mp3"):
            song = MP3(currently_loaded_song)
        elif (fileType == "flac"):
            song = FLAC(currently_loaded_song)
        else:
            print("Unsupported file type")
            return 0
        
        songLength = song.info.length
        current_position = pygame.mixer.music.get_pos() / 1000
        progress = (current_position / songLength) * 100
        return progress
    else:
        return 0
