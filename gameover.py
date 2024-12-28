import sys
import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 300))

image = pygame.image.load(os.path.join('data', 'gameover.png'))
image_rect = image.get_rect()
image_rect.x = -600

clock = pygame.time.Clock()

speed = 200

while True:
    delta_time = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    movement = speed * delta_time
    image_rect.x += movement

    if image_rect.x >= 0:
        speed = 0
        image_rect.x = 0

    screen.fill('blue')
    screen.blit(image, image_rect)
    pygame.display.flip()
