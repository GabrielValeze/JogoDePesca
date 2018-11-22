import pygame

colisao = False

class Peixe(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("fish1.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def mover(self,vel):

        self.rect.x += vel

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def empilhar(self):
        self.rect.x += 38
        self.rect.y += 19

