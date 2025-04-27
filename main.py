import pygame
from pygame.locals import *

# Inicjalizacja PyGame
pygame.init()

# Ekran telefonu (dostosuj rozdzielczość)
screen = pygame.display.set_mode((400, 600), FULLSCREEN)
clock = pygame.time.Clock()

# Pozycja kwadratu
x, y = 200, 300
speed = 5

running = True
while running:
    screen.fill((0, 0, 0))  # Czarne tło

    # Rysuj kwadrat
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

    # Obsługa zdarzeń (dotyk i wyjście)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # Przesuń kwadrat w miejsce dotknięcia
            x, y = event.pos[0] - 25, event.pos[1] - 25

    pygame.display.update()
    clock.tick(60)

pygame.quit()