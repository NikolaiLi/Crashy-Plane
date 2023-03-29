import pygame

class Plane(pygame.sprite.Sprite):
    def __init__(self, width, height, screen):
        super().__init__()
        planesize = (50,50)
        self.screen = screen
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("plane.png")
        self.image = pygame.transform.scale(self.image, planesize)
        self.velocity = 3
        self.velocity1 = 8
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

        
    # Vi giver klassen to funktioner til bevægelse op/ned. 
    # I hver funktion opdatere vi rectens y position og tjekker at vi ikke bevæger os udover spillets ramme/skærm
    def moveUp(self):

        self.rect.y -= self.velocity
        if self.rect.y < 0:
            self.rect.y = 0
          
    def moveDown(self):
        if self.rect.y < 0:
            self.rect.y = 0

        self.rect.y += self.velocity
       
        if self.rect.y > self.screen.get_height()-self.rect.height:
            self.rect.y = self.screen.get_height()-self.rect.height
