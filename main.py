import sys
import sword
import pygame
import ctypes

pygame.init()

sword = sword.Sword()
sword.save("temp.png")
sword_image = pygame.image.load("temp.png")
screen = pygame.display.set_mode((110, 110))
scaled_image = pygame.transform.scale(sword_image, (sword_image.get_width() * 10, sword_image.get_height() * 10))

while True:
    screen.blit(scaled_image, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()