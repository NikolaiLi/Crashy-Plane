# Importer pygame library og klasser
import pygame
from plane import Plane
from towers import Towers
from random import randint, choice

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crashy Plane")

# Models
# Opretter variable til at gemme spillernes score
score = 0
dead = "You died"
deathScreen = False

# Opretter spiller
spiller = Plane(50, 50, screen)
spiller.rect.x = 100
spiller.rect.y = 200


objekt = Towers(70, 300, screen)
objekt.rect.x = 300
objekt.rect.y = 300

# Denne liste skal indeholde alle spil-objekter
all_sprites_list = pygame.sprite.Group()
 
# Her skal spil-objekterne tilføjes
all_sprites_list.add(spiller)
all_sprites_list.add(objekt)
running = True

clock = pygame.time.Clock()

"""def death():
    
    deathScreen = True"""

    

# -------- Game Loop -----------
while running:
    currentTimer = pygame.time.get_ticks()
    score = int(currentTimer/720)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              running = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     running = False

    # --- Controller
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        spiller.moveUp()
    else:
        spiller.moveDown()
    objekt.moveLeft()

    """if spiller.rect.colliderect(objekt.rect):
        print("heeej")
        death()"""
    # Her kalder PyGame alle spil-objekter update()-metode
    all_sprites_list.update()

    # --- View
    screen.fill(BLACK)

    """if deathScreen == True:
        print("Death")
        font = pygame.font.Font(None, 74)
        text = font.render(str(dead), 1, WHITE)
        screen.blit(text, (325,20)) """
    # Her tegnes alle spil-objekter på skærmen screen
    all_sprites_list.draw(screen)
 
    #Her tegnes scoren
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, WHITE)
    screen.blit(text, (325,10))
 
    # --- Flipper skærmen
    pygame.display.flip()
     
    # --- 60 FPS bliver sat på PyGames clock
    clock.tick(60)
    
    

#Spillet slutter hvis man kommer ud af gameloopet
pygame.quit()

