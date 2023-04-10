import pygame

pygame.init()

BLACK = (0,0,0)
BLUE = (135, 206, 235)
WHITE = (255,255,255)

screenwidth = (800)
screenheight = (500)
screen = pygame.display.set_mode((screenwidth,screenheight))

bg = pygame.image.load("newyork-city.png")
bgtrans = pygame.transform.scale(bg,(screenwidth,int(screenheight/4)))

tower_gap = 150
tower_freq = 1500
last_tower = pygame.time.get_ticks()


pygame.display.set_caption("Crashy Plane")



score = 0
dead = "You died"

class Plane(pygame.sprite.Sprite):
    def __init__(self, width, height, screen):
        super().__init__()
        planesize = (50,50)
        self.screen = screen
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("plane.png")
        self.image = pygame.transform.scale(self.image, planesize)
        self.velocity = 0
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = int(screenheight/2)
        self.get_pressed = False
        
    # Vi giver klassen to funktioner til bevægelse op/ned. 
    # I hver funktion opdatere vi rectens y position og tjekker at vi ikke bevæger os udover spillets ramme/skærm
    
    def update(self):
        
        self.velocity += 0.5
        if self.velocity > 8:
            self.velocity = 8
        if self.rect.bottom < screenheight:
            self.rect.y += int(self.velocity)
            
        if pygame.key.get_pressed()[pygame.K_SPACE] == 1 and self.get_pressed == False:
            self.get_pressed = True
            self.velocity = -10

        if pygame.key.get_pressed()[pygame.K_SPACE] == 0:
            self.get_pressed = False

        if spiller.rect.colliderect(top_tower.rect):
            self.velocity = 0
        elif spiller.rect.colliderect(btm_tower.rect):
            self.velocity = 0

class Towers(pygame.sprite.Sprite):
    def __init__(self, width, height, position, screen):
        super().__init__()
        towersize = (70,300)
        self.screen = screen
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("towers.png")
        self.image = pygame.transform.scale(self.image, towersize)
        self.velocity = 3
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 300

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [width, height - int(tower_gap / 2)]

        if position == -1:
            self.rect.topleft = [width, height + int(tower_gap / 2)]
        
    def update(self):
        self.rect.x -= self.velocity

        if spiller.rect.colliderect(top_tower.rect):
            self.velocity = 0
        elif spiller.rect.colliderect(btm_tower.rect):
            self.velocity = 0

        if self.rect.x < -70:
            self.kill()

# Opretter spiller
spiller = Plane(50, int(screenheight/2), screen)

# Denne liste skal indeholde alle spil-objekter
plane_group = pygame.sprite.Group()
tower_group = pygame.sprite.Group()

# Her skal spil-objekterne tilføjes
plane_group.add(spiller)
btm_tower = Towers(screenwidth, int(screenheight/2), -1, screen)
top_tower = Towers(screenwidth, int(screenheight/2), 1, screen)                                                   
tower_group.add(btm_tower)
tower_group.add(top_tower)

clock = pygame.time.Clock()

running = True
while running:
    currentTimer = pygame.time.get_ticks()
    score = int(currentTimer/720)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              running = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     running = False

    # --- View
    screen.fill(BLUE)
    screen.blit(bgtrans,(0,int(screenheight/1.32)))

    # Her tegnes alle spil-objekter på skærmen screen
    plane_group.draw(screen)
     # Her kalder PyGame alle spil-objekter update()-metode
    plane_group.update()
    tower_group.draw(screen)
    tower_group.update() 

    """time = int(currentTimer)
    if time == - last_tower > tower_freq:
    
        last_tower = time"""

    if spiller.rect.colliderect(top_tower.rect):
        deathScreen()
        
    elif spiller.rect.colliderect(btm_tower):
        deathScreen()

    

    #Her tegnes scoren
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, WHITE)
    screen.blit(text, (375,10))
 
    def deathScreen():
        font = pygame.font.Font(None, 74)
        text = font.render(str(dead), 1, WHITE)
        screen.blit(text, (400,250))   
    

    # --- Flipper skærmen
    pygame.display.flip()
     
    # --- 60 FPS bliver sat på PyGames clock
    clock.tick(60)
    
     
    

#Spillet slutter hvis man kommer ud af gameloopet
pygame.quit()









