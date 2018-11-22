import pygame
from Anzol import Anzol
from Peixe import Peixe
import time

alturaAnzol=47
larguraAnzol=485
largura = 800
altura = 350
alturapeixePilha=200
largurapeixePilha=150
qtdpeixe=0
sair=False
colisao = False

pygame.init()
Tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Pesca")
fonte = pygame.font.SysFont("monospace", 48)
fundo = pygame.image.load("cenario.jpg").convert_alpha()
Tela.blit(fundo, (0, 0))
listaSprite = pygame.sprite.Group()

anzol = Anzol(larguraAnzol, alturaAnzol)
pilha=Peixe(largurapeixePilha,alturapeixePilha)
peixe = Peixe(0,300)
listaSprite.add(anzol)
listaSprite.add(peixe)




while not sair:
    if pygame.sprite.collide_rect(anzol, peixe):
        colisao = True
        anzol.rect.x = larguraAnzol
        anzol.rect.y = alturaAnzol
        peixe.kill()
        listaSprite.add(pilha)
        qtdpeixe+=1
        print(qtdpeixe)


    if peixe.rect.x <= 800:
        time.sleep(0.01)
        peixe.mover(1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair=True
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE]:
            anzol.descer()
        if anzol.rect.y >= 300:
            anzol.rect.y = alturaAnzol
            anzol.rect.x = larguraAnzol


    pygame.display.update()
    Tela.blit(fundo, (0, 0))
    listaSprite.draw(Tela)



pygame.quit()

