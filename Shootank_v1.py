import pygame, sys

pygame.init()

ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)

class Tanque_p1(pygame.sprite.Sprite):
    def __init__(self,x,y ):
        super().__init__()

        self.image = pygame.Surface((50,50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.rect.topleft = (x, y)

    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.rect.y -= 5
        if teclas[pygame.K_DOWN]:
            self.rect.y += 5    
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5  

class Tanque_p2(Tanque_p1, pygame.sprite.Sprite):
    def update(self):
        teclas = pygame.key.get_pressed()        
        if teclas[pygame.K_w]:
            self.rect.y -= 5
        if teclas[pygame.K_s]:
            self.rect.y += 5    
        if teclas[pygame.K_d]:
            self.rect.x += 5
        if teclas[pygame.K_a]:
            self.rect.x -= 5    

class Bala(pygame.sprite.Sprite):
    def __init__(self, x,y,dueño,direccion):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(center=(x,y))
        self.rect.topleft = (x, y)



tanque_1 = Tanque_p1(0,700)
tanque_2 = Tanque_p2(500,700)
grup_tanque = pygame.sprite.Group(tanque_1, tanque_2)

jugando = True

clock = pygame.time.Clock()


while jugando:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    ventana.fill((0,0,0))

    grup_tanque.update()

    grup_tanque.draw(ventana)

    pygame.display.flip()
