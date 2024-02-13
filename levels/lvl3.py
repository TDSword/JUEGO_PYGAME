import pygame, random, sys
import math
from menu import button
from menu.general import BLACK, WHITE, GREEN, RED, BLUE, GRISACEO, CELESTE, ROSA, size,screen, trail, Nft, Player, draw_text


def empezar():
    pause = False
    music_playing = False
    lose = False
    vidas = 15
    puntaje = 0
    font = pygame.font.SysFont("arialblack", 25)

    line_angle = 90  # Ángulo inicial



    # Posición y velocidad inicial del círculo
    circle_radius = 20
    circle_pos = [100, 100]
    circle_speed = [5, 3]
    circle_pos2 = [700, 100]
    circle_speed2 = [-5, -3]

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
    pygame.mixer.music.load('assets/sounds/Common_exe.mp3')
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
            screen.blit(pygame.image.load("assets/images/fondolvl3.png").convert(), (0, 0))
            sprites_lista.draw(screen)



            # el jugador

            # Agregar la posición actual a la lista de estela (corregida para que sea acorde la png)
            trail.append((coor_x+22, coor_y+22))

            # Limitar la estela
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
            pygame.draw.rect(screen,GRISACEO, (13, 430, 60, 60))
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/borde2.png"), (60, 60)), (13, 430))
            draw_text(str(puntaje), font, WHITE, 30, 440)

                #intrucciones:
            if puntaje<4 and vidas > 0:
                draw_text("RECOJE MAS DE 25 ESTRELLAS!", pygame.font.SysFont("arialblack", 40), GREEN, 50, 130)


            #PELOTAS
            # Actualizar la posición del círculo
            circle_pos[0] += circle_speed[0]
            circle_pos[1] += circle_speed[1]
            circle_pos2[0] += circle_speed2[0]
            circle_pos2[1] += circle_speed2[1]

            # bordes horizontales
            if circle_pos[0] - circle_radius < 0 or circle_pos[0] + circle_radius > size[0]:
                circle_speed[0] = -circle_speed[0]
            if circle_pos2[0] - circle_radius < 0 or circle_pos2[0] + circle_radius > size[0]:
                circle_speed2[0] = -circle_speed2[0]

            # Verificar y corregir el rebote en los bordes verticales
            if circle_pos[1] - circle_radius < 0 or circle_pos[1] + circle_radius > size[1]:
                circle_speed[1] = -circle_speed[1]
            if circle_pos2[1] - circle_radius < 0 or circle_pos2[1] + circle_radius > size[1]:
                circle_speed2[1] = -circle_speed2[1]

            # Dibujar los ciculos
            pygame.draw.circle(screen, WHITE, (int(circle_pos2[0]), int(circle_pos2[1])), circle_radius)
            pygame.draw.circle(screen, WHITE, (int(circle_pos[0]), int(circle_pos[1])), circle_radius)

            # colisiones (y dibujado)
            if _ := pygame.draw.circle(screen, WHITE, (int(circle_pos[0]), int(circle_pos[1])), circle_radius).colliderect(pygame.Rect(coor_x, coor_y, 32, 32)) and operandi != "lento":
                coor_x = 400
                coor_y = 250
                vidas -= 1

            if _ := pygame.draw.circle(screen, WHITE, (int(circle_pos2[0]), int(circle_pos2[1])), circle_radius).colliderect(pygame.Rect(coor_x, coor_y, 32, 32)) and operandi != "lento":
                coor_x = 400
                coor_y = 250
                vidas -= 1


            # LINEA FIJA
            if _ := pygame.draw.rect(screen, ROSA, (0, 100, 800, 5)).colliderect(pygame.Rect(coor_x, coor_y, 32, 32)) and operandi != "rapido":
                coor_x = 400
                coor_y = 250
                vidas -= 1


            # LINEA GIRADORA

            line_end_x = 150 + 500 * math.cos(math.radians(line_angle))
            line_end_y = 250 + 500 * math.sin(math.radians(line_angle))
            #colisiones (y dibujado)
            if _ := pygame.draw.line(screen, CELESTE, (150, 250), (line_end_x, line_end_y), 1).colliderect(pygame.Rect(coor_x, coor_y, 1, 1)) and operandi != "lento":
                coor_x = 400
                coor_y = 250
                vidas -= 1

            #aumentar el angulo de la linea
            line_angle += 1


            # NFTs

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
            # Comprobar si el jugador terminó
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/cuadro.png"), (500+500/7, 300+300/7)), (150-500/14, 100-300/14))
            draw_text(f"PUNTAJE: {puntaje}", pygame.font.SysFont("arialblack", 40), BLACK, 280, 180)

            if puntaje<25:
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


            # que pasa x boton
            if restart_button.draw(screen):
                empezar()

            if menu_button.draw(screen):
                lose=True

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(30)
    lose = False
