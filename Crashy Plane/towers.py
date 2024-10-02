import pygame

class Towers(pygame.sprite.Sprite):
    def __init__(self, width, height, screen):
        super().__init__()
        towersize = (70,300)
        self.screen = screen
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("towers.png")
        self.image = pygame.transform.scale(self.image, towersize)
        self.velocity = 3
        self.velocity1 = 8
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 300
        
    def moveLeft(self):
        self.rect.x -= self.velocity
       
        if self.rect.x > self.screen.get_width()-self.rect.width:
            self.rect.x = self.screen.get_width()-self.rect.width