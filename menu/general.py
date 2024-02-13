import pygame

# Colores

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRISACEO = (55, 52, 55)
CELESTE = (146, 221, 220)
ROSA = (216, 109, 132)

# pantalla
size = (800, 500)
screen = pygame.display.set_mode(size)
trail = []

# dibujo
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Nft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("assets/images/nft.png")
        self.image = pygame.transform.scale(original_image, (40, 40))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/images/jugador.png"), (45, 45)).convert_alpha()
        self.rect = self.image.get_rect()