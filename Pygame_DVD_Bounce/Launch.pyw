# Ethan Frailey
# Date
# Project

# Imports
import pygame
import tkinter as TK
import os

# setup folder assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Images")
sprites_folder = os.path.join(img_folder, "Sprites")
sounds_folder = os.path.join(game_folder, "Sounds")
text_folder = os.path.join(game_folder, "Text")

player_img = pygame.image.load(os.path.join(img_folder, "DVD Bounce.png")).convert()


# Specifications
root = TK.Tk()
TITLE = "My PyGame"
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
FPS = 90

# Colors (R G B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PEACH = (235, 64, 52)
MORINING = (252, 186, 3)
Purple = (255, 0, 225)
OCEAN = (66, 135, 245)
GRASS = (50, 168, 82)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# Game Classes
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        # self.image = pygame.Surface((25, 25))
        self.image = player_img
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 2
        self.speedy = 2

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left <= 0:
            self.speedx *= -1
        if self.rect.right >= WIDTH:
            self.speedx *= -1
        if self.rect.top <= 0:
            self.speedy *= -1
        if self.rect.bottom >= HEIGHT:
            self.speedy *= -1



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(MORINING)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0
        self.keypressed = False

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_s]:
            self.speedy = 5

        self.rect.x += self.speedx
        self.rect.y += self.speedy

# We are binding it to the screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT



# Sprite Group
all_sprites = pygame.sprite.Group()
players_group = pygame.sprite.Group()
mobs_group = pygame.sprite.Group()

# Create Game Objects
Block = NPC()
player = Player()

# add objects to s[rite groups
all_sprites.add(player)
players_group.add(player)
all_sprites.add(Block)
all_sprites.add(Block)

# Game Loop
running = True
while running:
    clock.tick(FPS)

    mousex, mousey = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

quit()
