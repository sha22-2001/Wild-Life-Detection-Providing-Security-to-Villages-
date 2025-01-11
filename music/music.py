import pygame

audio_path = r"D:\PROJECT_EXPO\music\2.wav"

pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play(-1)

while True:
    pygame.time.wait(50)
