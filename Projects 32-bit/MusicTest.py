import pygame
import time
my_song = "the-mask-horn.wav"
# pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(my_song)
pygame.mixer.music.play()
time.sleep(10)

# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
