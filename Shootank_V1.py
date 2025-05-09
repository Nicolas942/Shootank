import pygame, sys, random

pygame.init()
ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)

fuente_arial_name = pygame.font.SysFont("arial", 100, 1, 1)
fuente_arial_integrantes = pygame.font.SysFont("arial", 20, 1, 1)
fuente_arial_ganador = pygame.font.SysFont("arial", 50, 1, 1)

class Tanque_p1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = "UP"
        self.vidas = 5
        self.ultimo_disparo = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.rect.y -= 3
            self.direccion = "UP"
        if teclas[pygame.K_DOWN]:
            self.rect.y += 3
            self.direccion = "DOWN"
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 3
            self.direccion = "RIGHT"
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 3
            self.direccion = "LEFT"
        if teclas[pygame.K_KP_ENTER]:
            self.disparar(balas)
        self.rect.clamp_ip(ventana.get_rect())

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= 500:
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)
            self.ultimo_disparo = tiempo_act

class Tanque_p2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = "UP"
        self.vidas = 5
        self.ultimo_disparo = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            self.rect.y -= 3
            self.direccion = "UP"
        if teclas[pygame.K_s]:
            self.rect.y += 3
            self.direccion = "DOWN"
        if teclas[pygame.K_d]:
            self.rect.x += 3
            self.direccion = "RIGHT"
        if teclas[pygame.K_a]:
            self.rect.x -= 3
            self.direccion = "LEFT"
        if teclas[pygame.K_SPACE]:
            self.disparar(balas)
        self.rect.clamp_ip(ventana.get_rect())

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= 500:
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)
            self.ultimo_disparo = tiempo_act

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, dueño):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = direccion
        self.velocidad = 10
        self.dueño = dueño

    def update(self):
        if self.direccion == "UP":
            self.rect.y -= self.velocidad
        if self.direccion == "DOWN":
            self.rect.y += self.velocidad
        if self.direccion == "RIGHT":
            self.rect.x += self.velocidad
        if self.direccion == "LEFT":
            self.rect.x -= self.velocidad
        if not ventana.get_rect().colliderect(self.rect):
            self.kill()

class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=(random.randint(50, 1300), random.randint(50, 700)))

tanque_1 = Tanque_p1(0, random.randint(0, 780))
tanque_2 = Tanque_p2(1366, random.randint(0, 780))

grup_tanque = pygame.sprite.Group(tanque_1, tanque_2)
balas = pygame.sprite.Group()
poderes = pygame.sprite.Group()

clock = pygame.time.Clock()
jugando = True
ganador = None
juego_terminado = False
ultimo_tiempo_poder = 0

while jugando:
    clock.tick(60)
    tiempo_actual = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

    if tiempo_actual < 3000:
        ventana.fill((0, 0, 0))
        ventana.blit(fuente_arial_name.render("Shotank", True, (255, 255, 255)), (480, 50))
        ventana.blit(fuente_arial_integrantes.render("Nicolás Alfonso Cabrera Suárez", True, (255, 255, 255)), (525, 170))
        ventana.blit(fuente_arial_integrantes.render("Daniel Alejandro Rios Rincon", True, (255, 255, 255)), (535, 200))
        ventana.blit(fuente_arial_integrantes.render("Daniel Felipe Diaz Fontecha", True, (255, 255, 255)), (540, 230))
    else:
        ventana.fill((0, 255, 0))

        # Generar un poder solo si no hay otro
        if len(poderes) == 0 and tiempo_actual - ultimo_tiempo_poder > 5000:
            nuevo_poder = Power()
            poderes.add(nuevo_poder)
            ultimo_tiempo_poder = tiempo_actual

        if not juego_terminado:
            grup_tanque.update()
            balas.update()
            grup_tanque.draw(ventana)
            balas.draw(ventana)
            poderes.draw(ventana)

            for bala in balas:
                if bala.dueño != tanque_1 and bala.rect.colliderect(tanque_1.rect):
                    tanque_1.vidas -= 1
                    bala.kill()
                    if tanque_1.vidas <= 0:
                        tanque_1.kill()
                        ganador = "Tanque 2"
                        juego_terminado = True

                if bala.dueño != tanque_2 and bala.rect.colliderect(tanque_2.rect):
                    tanque_2.vidas -= 1
                    bala.kill()
                    if tanque_2.vidas <= 0:
                        tanque_2.kill()
                        ganador = "Tanque 1"
                        juego_terminado = True

            # Recoger poder 
            for tanque in grup_tanque:
                for power in poderes:
                    if tanque.rect.colliderect(power.rect):
                        poderes.remove(power)
                        
        else:
            ventana.fill((0, 0, 0))
            ventana.blit(fuente_arial_name.render("Fin del juego", True, (255, 255, 255)), (340, 200))
            ventana.blit(fuente_arial_ganador.render(f"{ganador} es el ganador", True, (255, 255, 255)), (360, 330))

    pygame.display.flip()


