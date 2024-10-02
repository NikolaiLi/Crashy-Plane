import pygame

flying = False

class Plane(pygame.sprite.Sprite):
    def __init__(self, width, height, screen):
        super().__init__()
        planesize = (50,50)
        self.screen = screen
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("plane.png")
        self.image = pygame.transform.scale(self.image, planesize)
        self.velocity = 0
        self.velocity1 = 8
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.get_pressed = False
        
    # Vi giver klassen to funktioner til bevægelse op/ned. 
    # I hver funktion opdatere vi rectens y position og tjekker at vi ikke bevæger os udover spillets ramme/skærm
    
    def update(self):
        
        self.velocity += 0.5
        if self.velocity > 8:
            self.velocity = 8
        if self.rect.bottom < 500:
            self.rect.y += int(self.velocity)
            
        if pygame.key.get_pressed()[pygame.K_SPACE] == 1 and self.get_pressed == False:
            self.get_pressed = True
            self.velocity = -10

        if pygame.key.get_pressed()[pygame.K_SPACE] == 0:
            self.get_pressed = False
    
        
    
    
    def moveUp(self):

        """if pygame.key.get_pressed()[pygame.K_SPACE] == 1 and self.get_pressed == False:
            self.get_pressed = True
            self.velocity = -10

        if pygame.key.get_pressed()[pygame.K_SPACE] == 0:
            self.get_pressed = False"""


        """self.rect.y -= self.velocity1
        if self.rect.y < 0:
            self.rect.y = 0"""
          
    def moveDown(self):
        """self.velocity += 0.5
        if self.velocity > 8:
            self.velocity = 8
        if self.rect.bottom < 500:
            self.rect.y += int(self.velocity)"""


        """if self.rect.y < 0:
            self.rect.y = 0

        self.rect.y += self.velocity

        if self.rect.y > self.screen.get_height()-self.rect.height:
            self.rect.y = self.screen.get_height()-self.rect.height"""
