import pygame, sys, random

from levels import lvl1, lvl2, lvl3
from menu import button
from menu.general import screen, draw_text


def play_music_menu():
    pygame.mixer.music.load('assets/sounds/OST_MENU.mp3')
    pygame.mixer.music.play(0)

run = True

pygame.init()

pygame.display.set_caption("CryptoTrail Runner")

# importe de botones a usar:
quit_img = pygame.transform.scale(pygame.image.load("assets/images/buttonquit.png"), (200-200/8, 75-75/8)).convert_alpha()
quit_button = button.Button(75, 370, quit_img, 1)

play_img = pygame.transform.scale(pygame.image.load("assets/images/buttonplay.png"), (200-200/8, 75-75/8)).convert_alpha()
play_button = button.Button(525, 370, play_img, 1)

logo_img = pygame.transform.scale(pygame.image.load("assets/images/logo.jpg"), (300, 300)).convert_alpha()
logo_button = button.Button(250, 80, logo_img, 1)

menu_img = pygame.transform.scale(pygame.image.load("assets/images/buttonmenu.png"), (200-200/8, 75-75/8)).convert_alpha()
menu_button = button.Button(150, 150, menu_img, 1)

lvl1_img = pygame.transform.scale(pygame.image.load("assets/images/buttonlvl1.png"), (200-200/8, 75-75/8)).convert_alpha()
lvl1_button = button.Button(450, 150, lvl1_img, 1)

lvl2_img = pygame.transform.scale(pygame.image.load("assets/images/buttonlvl2.png"), (200-200/8, 75-75/8)).convert_alpha()
lvl2_button = button.Button(150, 300, lvl2_img, 1)

lvl3_img = pygame.transform.scale(pygame.image.load("assets/images/buttonlvl3.png"), (200-200/8, 75-75/8)).convert_alpha()
lvl3_button = button.Button(450, 300, lvl3_img, 1)

play_music_menu()

menumodo = "inicial"

while run:

    screen.fill((0, 0, 0))
    draw_text("CryptoTrail Runner", pygame.font.SysFont("arialblack", 40), (200,200,200), 200, 20)
    # que pasa x boton

    if menumodo == "inicial":


        if quit_button.draw(screen):
            run = False

        if logo_button.draw(screen):
            print("Hola mundo")

        if play_button.draw(screen):
            menumodo = "niveles"

    elif menumodo == "niveles":
        if menu_button.draw(screen):
            menumodo = "inicial"

        if lvl1_button.draw(screen):
            lvl1.empezar()
            menumodo = "inicial"
            play_music_menu()

        if lvl2_button.draw(screen):
            lvl2.empezar()
            menumodo = "inicial"
            play_music_menu()
        
        if lvl3_button.draw(screen):
            lvl3.empezar()
            menumodo = "inicial"
            play_music_menu()


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()