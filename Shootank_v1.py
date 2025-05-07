import pygame, sys

pygame.init()

ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)

class tanque(pygame.sprite.Sprite):
    def __init__(self,x,y ):
        super().__init__()

        self.image = pygame.surface((50,50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.rect.topleft = (100, 100)



jugando = True


while jugando:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            

    ventana.fill((0,0,0))

    pygame.display.flip()
