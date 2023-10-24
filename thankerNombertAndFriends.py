import time
import os
import sys
import random
import math
import pygame
from pygame.locals import *
from pygame import mixer
from pygame.locals import *

# inicializa pygame
pygame.init()
mixer.init()
# inicializa el modulo de sonido
pygame.mixer.init()
# establece el volumen
pygame.mixer.music.set_volume(0.9)

# establece el tamaño de la ventana
size = width, height = 1400, 900
# establece el color de la ventana
black = 0, 0, 0
# establece el color de la ventana
white = 255, 255, 255
# establece el color de la ventana
red = 255, 0, 0
# establece el color de la ventana
green = 0, 255, 0
# establece el color de la ventana
blue = 0, 0, 255
# establece el color de la ventana
yellow = 255, 255, 0
# establece el color de la ventana
purple = 255, 0, 255
# establece el color de la ventana
cyan = 0, 255, 255
# establece el color de la ventana
orange = 255, 128, 0
# establece el color de la ventana
pink = 255, 0, 128
# establece el color de la ventana
brown = 102, 51, 0


colors = [red, green, blue, yellow, white, purple, cyan, orange, pink, brown]

# establece el tamaño de la ventana
screen = pygame.display.set_mode(size)
# establece el titulo de la ventana
pygame.display.set_caption("Saddie Pinn")
# establece el color de la ventana
screen.fill(black)
# establece el icono de la ventana
icon = pygame.image.load("icon.jpeg")
pygame.display.set_icon(icon)



# animacion ascii art con el nombre de saddie pinn
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# animacion ascii art con el nombre de saddie pinn
def ascii_art():
    clear()
    print(" ")
    print(" ")
    print("  _______  _______  _______  _______  _______  _______  _______  _______  _______ ")
    print(" (  ____ \(  ___  )(       )(  ____ \(  ____ \(  ____ \(  ____ \(  ____ \(  ____ )")
    print(" | (    \/| (   ) || () () || (    \/| (    \/| (    \/| (    \/| (    \/| (    )|")
    print(" | |      | |   | || || || || (__    | (__    | (__    | (__    | (__    | (____)|")
    print(" | | ____ | |   | || |(_)| ||  __)   |  __)   |  __)   |  __)   |  __)   |     __)")
    print(" | | \_  )| |   | || |   | || (      | (      | (      | (      | (      | (\ (   ")
    print(" | (___) || (___) || )   ( || (____/\| (____/\| (____/\| (____/\| (____/\| ) \ \__")
    print(" (_______)(_______)|/     \|(_______/(_______/(_______/(_______/(_______/|/   \__/")
    print(" ")
    print(" ")

def ascii_art_juego():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Gomeeeeer', True, white, black)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)
    screen.blit(text, textRect)
    pygame.display.update()
    time.sleep(3)


class AsciiArtAnimation:
    def __init__(self, screen, width, height, string, colors):
        self.screen = screen
        self.width = width
        self.height = height
        self.colors = colors
        self.x = self.width // 2
        self.y = self.height // 2
        self.directionX = 1
        self.directionY = 1
        self.directionChangeCycles = 0
        self.string = string
        self.color = random.choice(self.colors)

    def render_ascii_art(self):
        string = self.string
        color = self.color
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render(string, True, color, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        self.screen.blit(text, textRect)

    def update_position(self):
        self.x += self.directionX
        self.y += self.directionY
        self.directionChangeCycles -= 1

        if self.x > self.width or self.x < 0:
            self.directionX = -self.directionX

        if self.y > self.height or self.y < 0:
            self.directionY = -self.directionY

        if self.directionChangeCycles <= 0:
            self.directionChangeCycles = random.randint(10, 100)
            self.directionX = random.randint(-1, 1)
            self.directionY = random.randint(-1, 1)
            self.color = random.choice(self.colors)

def main():
    global colors 
    strings = ['GOMEEEEER', 'THANKER NOMBERT', 'SADDIE PINN', 'GO', 'KURSKAL', 'CONDENA', 'SCIPY', 'BUFFER','RATS','REPARSER', 'NIVEL DE TRANSPORTE']
    ascii_animations = [AsciiArtAnimation(screen, width, height, s, colors) for s in strings]


    while True:
        for a in ascii_animations:
            a.render_ascii_art()
            a.update_position()
        pygame.display.update()
        

if __name__ == "__main__":
    main()
