import pygame, random, sys
import math
from menu import button
from menu.general import BLACK, WHITE, GREEN, RED, BLUE, GRISACEO, CELESTE, ROSA, screen, trail, Nft, Player, draw_text

# Clases


def empezar():
    pause = False
    music_playing = False
    lose = False
    vidas = 10
    puntaje = 0
    font = pygame.font.SysFont("arialblack", 25)


    # boton de reanudar
    restart_img = pygame.transform.scale(pygame.image.load("assets/images/buttonrestart.png"), (200, 75)).convert_alpha()
    restart_button = button.Button(445, 275, restart_img, 1)
    # boton de menu (perder)
    menu_img = pygame.transform.scale(pygame.image.load("assets/images/buttonmenu.png"), (200, 75)).convert_alpha()
    menu_button = button.Button(155, 275, menu_img, 1)

    # Grupos de sprites
    nft_lista = pygame.sprite.Group()
    sprites_lista = pygame.sprite.Group()

    # Crear instancias de Nft y agregarlas a los grupos
    for _ in range(2):
        nft = Nft()
        nft.rect.x = random.randrange(800)
        nft.rect.y = random.randrange(500)
        nft_lista.add(nft)
        sprites_lista.add(nft)

    # Crear instancia de Player y agregarla al grupo
    player = Player()
    sprites_lista.add(player)

    # Configuración del reloj
    clock = pygame.time.Clock()

    # Coordenadas y velocidades
    coor_x = 400
    coor_y = 250
    linea_y = 0
    x_speed = 0
    y_speed = 0
    linea_speed = 3
    modo = 5
    operandi = "normal"

    # Música
    pygame.mixer.music.load('assets/sounds/Iron_Knight_Gamma_exe.mp3')
    pygame.mixer.music.play(0)

    # Bucle principal
    while not lose:
        for event in pygame.event.get():
            if pause == False and vidas >= 0:
                if event.type == pygame.QUIT:
                    lose = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_speed = -modo
                        y_speed = 0
                    elif event.key == pygame.K_RIGHT:
                        x_speed = modo
                        y_speed = 0
                    elif event.key == pygame.K_UP:
                        y_speed = -modo
                        x_speed = 0
                    elif event.key == pygame.K_DOWN:
                        y_speed = modo
                        x_speed = 0
                    elif event.key == pygame.K_SPACE:
                        modo = 2
                        operandi = "lento"
                    elif event.key == pygame.K_c:
                        operandi = "rapido"
                        modo = 26
                    elif event.key == pygame.K_ESCAPE:
                        pause = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_ESCAPE:
                        pass
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_c:
                        operandi = "normal"
                        modo = 5

            elif pause == True and vidas > 0:
                if event.type == pygame.QUIT:
                    lose = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        pause = False
            else:
                if event.type == pygame.QUIT:
                    lose = True
        if pause == False and vidas >= 0:
            # Lógica del juego
            if coor_x > 800 or coor_x < 0 or coor_y > 500 or coor_y < 0:
                coor_x = 400
                coor_y = 250

            if abs(modo) > 15:
                coloreado = RED
            elif modo == 5:
                coloreado = GREEN
            else:
                coloreado = BLUE

            coor_x += x_speed
            coor_y += y_speed

            linea_y += linea_speed
            if linea_y > 500:
                linea_y = 0

            player.rect.x = coor_x
            player.rect.y = coor_y

            # Dibujar en la pantalla

            screen.fill(GRISACEO)
            screen.blit(pygame.image.load("assets/images/fondolvl2.png").convert(), (0, 0))
            sprites_lista.draw(screen)



            # el jugador

            # Agregar la posición actual a la lista de estela (corregida para que sea acorde la png)
            trail.append((coor_x+22, coor_y+22))

            # Limitar la longitud de la estela para evitar un uso excesivo de memoria
            if len(trail) > 10:
                trail.pop(0)
            # Dibujar la estela
            for pos in trail:
                pygame.draw.circle(screen, WHITE, pos, 5)


            # Indicadores (velocidad, vidas)
            # vidas/estado
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/borde.png"), (60, 60)), (13, 13))
            pygame.draw.rect(screen, coloreado, (20, 20, 47, 47))
            draw_text(str(vidas), font, BLACK, 30, 25)

            # puntos
            pygame.draw.rect(screen, GRISACEO, (13, 430, 60, 60))
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/borde2.png"), (60, 60)), (13, 430))
            draw_text(str(puntaje), font, WHITE, 30, 440)

            pygame.draw.rect(screen, CELESTE, (0, linea_y, 800, 5))
            pygame.draw.rect(screen, ROSA, (300, 0, 8, 500))


            #intrucciones:
            if puntaje<4 and vidas > 0:
                draw_text("RECOJE MAS DE 10 ESTRELLAS!", pygame.font.SysFont("arialblack", 40), GREEN, 50, 130)

            # Colisiones

            if _ := pygame.Rect(0, linea_y, 800, 5).colliderect(pygame.Rect(coor_x, coor_y, 32, 32)) and operandi != "lento":
                coor_x = 400
                coor_y = 250
                vidas -= 1

            if _ := pygame.Rect(300, 0, 8, 500).colliderect(pygame.Rect(coor_x, coor_y, 32, 32)) and operandi != "rapido":
                coor_x = 400
                coor_y = 250
                vidas -= 1


            nft_recolectados = pygame.sprite.spritecollide(player, nft_lista, True)

            for _ in nft_recolectados:
                puntaje += 1
                nft = Nft()
                nft.rect.x = random.randrange(125,625)
                nft.rect.y = random.randrange(125,325)
                nft_lista.add(nft)
                sprites_lista.add(nft)

        elif pause == True and vidas >= 0:
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/cuadro.png"), (500+500/7, 300+300/7)), (150-500/14, 100-300/14))
            draw_text("PAUSE", pygame.font.SysFont("arialblack", 40), CELESTE, 310, 130)
            draw_text("[PRESS SPACE]", pygame.font.SysFont("arialblack", 40), CELESTE, 250, 200)
            if menu_button.draw(screen):
                lose=True
            if restart_button.draw(screen):
                empezar()
        else:
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/cuadro.png"), (500+500/7, 300+300/7)), (150-500/14, 100-300/14))
                        # Comprobar si el jugador terminó
            draw_text(f"PUNTAJE: {puntaje}", pygame.font.SysFont("arialblack", 40), BLACK, 280, 180)

            if puntaje<10:
                if not music_playing:
                    pygame.mixer.music.load('assets/sounds/sad.mp3')
                    pygame.mixer.music.play(0)
                    music_playing = True
                draw_text("PERDIÓ", pygame.font.SysFont("arialblack", 40), RED, 310, 130)

            else:
                if not music_playing:
                    pygame.mixer.music.load('assets/sounds/win.mp3')
                    pygame.mixer.music.play(0)
                    music_playing = True
                draw_text("HAS GANDADO!", pygame.font.SysFont("arialblack", 40), GREEN, 250, 130)


            # screen.blit(pygame.transform.scale(pygame.image.load("assets/images/cuadro.png"), (500, 300)), (150, 100))
            # que pasa x boton
            if restart_button.draw(screen):
                empezar()

            if menu_button.draw(screen):
                lose=True

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(30)
    lose = False
