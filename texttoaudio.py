from gtts import gTTS
import os
from datetime import datetime
import pygame
import time
import random
# Get the current date and time
current_datetime = datetime.now()

# Format the date and time to create a unique file name
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

# Create the file name
file_name = f"output_{formatted_datetime}_{random.randint(2,8)}.mp3"

def convert_text_to_speech(text, lang='hi', output_file=file_name):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)
    return output_file

def play_mp3(mp3_filename):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

