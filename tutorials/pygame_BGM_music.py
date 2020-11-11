import pygame

music_file = "sound/mybgm.mp3"

pygame.mixer.init()

# pygame.mixer.music = pygame.mixer.music
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

# pygame.mixer.music.stop()

clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
    clock.tick(30)

pygame.mixer.quit()
