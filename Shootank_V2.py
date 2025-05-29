import pygame, sys, random

pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((1000, 700))

fuente_arial_name = pygame.font.SysFont("arial", 100, 1, 1)
fuente_arial_integrantes = pygame.font.SysFont("arial", 20, 1, 1)
fuente_arial_ganador = pygame.font.SysFont("arial", 50, 1, 1)


# Imagenes (sprites)
logo = pygame.image.load("img/logo.png").convert()
logo = pygame.transform.scale(logo, (530, 370))
tanque_morado = pygame.image.load("img/tanque_morado.png")
tanque_morado = pygame.transform.scale(tanque_morado, (50, 50))
tanque_naranja = pygame.image.load("img/tanque_naranja.png")
tanque_naranja = pygame.transform.scale(tanque_naranja, (50, 50))
arbol_seco = pygame.image.load("img/arbol_seco.png")
arbol_seco = pygame.transform.scale(arbol_seco, (76, 92))
arbusto_vertical = pygame.image.load("img/arbusto_vertical.png")
arbusto_vertical = pygame.transform.scale(arbusto_vertical, (58, 113))
roca = pygame.image.load("img/roca.png")
roca = pygame.transform.scale(roca, (93, 61))
tree = pygame.image.load("img/tree.png")
tree = pygame.transform.scale(tree, (60, 60))
mas_vida = pygame.image.load("img/heart.png")
mas_vida = pygame.transform.scale(mas_vida, (18,16))
vida = pygame.image.load("img/heart.png")
vida = pygame.transform.scale2x(mas_vida)
bala_png = pygame.image.load("img/bala.png")
bala_png = pygame.transform.scale(bala_png, (20,20))
ametralladora = pygame.image.load("img/ametralladora.png")
ametralladora = pygame.transform.scale(ametralladora, (30,30))
escudo = pygame.image.load("img/escudo.png")
escudo = pygame.transform.scale(escudo, (30,30))
velocidad_poder = pygame.image.load("img/Zapato.png")
velocidad_poder = pygame.transform.scale(velocidad_poder, (30,30))

#Sonidos
pygame.mixer.music.load("Sounds/musica_fondo.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.5)

colicion_bala = pygame.mixer.Sound("Sounds/colicion_bala.ogg")
disparo = pygame.mixer.Sound("Sounds/disparo.ogg")
movimiento = pygame.mixer.Sound("Sounds/movimiento.ogg")
powerUP = pygame.mixer.Sound("Sounds/powerUP.ogg")


class Tanque_p1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_original = tanque_morado
        self.image = self.image_original
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = "UP"
        self.velocidad = 3
        self.vidas = 3
        self.ultimo_disparo = 0
        self.tiempo_velocidad = 0
        self.tiempo_disparo = 500
        self.tiempo_velocidad_disparo = 0
        self.escudo = False
        self.tiempo_escudo = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        posicion_anterior = self.rect.topleft
        if teclas[pygame.K_UP]:
            self.image = pygame.transform.rotate(self.image_original, 0)
            movimiento.play()
            self.rect.y -= self.velocidad
            self.direccion = "UP"
        if teclas[pygame.K_DOWN]:
            self.image = pygame.transform.rotate(self.image_original, 180)
            movimiento.play()
            self.rect.y += self.velocidad
            self.direccion = "DOWN"
        if teclas[pygame.K_RIGHT]:
            self.image = pygame.transform.rotate(self.image_original, 270)
            movimiento.play()
            self.rect.x += self.velocidad
            self.direccion = "RIGHT"
        if teclas[pygame.K_LEFT]:
            self.image = pygame.transform.rotate(self.image_original, 90)
            movimiento.play()
            self.rect.x -= self.velocidad
            self.direccion = "LEFT"
        if teclas[pygame.K_RETURN]:
            disparo.play()
            self.disparar(balas)

        if pygame.sprite.spritecollideany(self, obstaculos_group) or self.rect.colliderect(tanque_2.rect):
            self.rect.topleft = posicion_anterior

        if self.velocidad > 3 and pygame.time.get_ticks() - self.tiempo_velocidad > 5000:
            self.velocidad = 3
        if self.tiempo_disparo <= 500 and pygame.time.get_ticks() - self.tiempo_velocidad_disparo > 10000:
            self.tiempo_disparo = 500
        if self.escudo and pygame.time.get_ticks() - self.tiempo_escudo > 10000:
            self.escudo = False

        self.rect.clamp_ip(ventana.get_rect())

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= self.tiempo_disparo:
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)
            self.ultimo_disparo = tiempo_act


class Tanque_p2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_original = tanque_naranja
        self.image = self.image_original
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = "UP"
        self.velocidad = 3
        self.vidas = 3
        self.ultimo_disparo = 0
        self.tiempo_velocidad = 0
        self.tiempo_disparo = 500
        self.tiempo_velocidad_disparo = 0
        self.escudo = False
        self.tiempo_escudo = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        posicion_anterior = self.rect.topleft
        if teclas[pygame.K_w]:
            self.image = pygame.transform.rotate(self.image_original, 0)
            movimiento.play()
            self.rect.y -= self.velocidad
            self.direccion = "UP"
        if teclas[pygame.K_s]:
            self.image = pygame.transform.rotate(self.image_original, 180)
            movimiento.play()
            self.rect.y += self.velocidad
            self.direccion = "DOWN"
        if teclas[pygame.K_d]:
            self.image = pygame.transform.rotate(self.image_original, 270)
            movimiento.play()
            self.rect.x += self.velocidad
            self.direccion = "RIGHT"
        if teclas[pygame.K_a]:
            self.image = pygame.transform.rotate(self.image_original, 90)
            movimiento.play()
            self.rect.x -= self.velocidad
            self.direccion = "LEFT"
        if teclas[pygame.K_SPACE]:
            disparo.play()
            self.disparar(balas)

        if pygame.sprite.spritecollideany(self, obstaculos_group) or self.rect.colliderect(tanque_1.rect):
            self.rect.topleft = posicion_anterior

        if self.velocidad > 3 and pygame.time.get_ticks() - self.tiempo_velocidad > 5000:
            self.velocidad = 3
        if self.tiempo_disparo <= 500 and pygame.time.get_ticks() - self.tiempo_velocidad_disparo > 10000:
            self.tiempo_disparo = 500
        if self.escudo and pygame.time.get_ticks() - self.tiempo_escudo > 10000:
            self.escudo = False

        self.rect.clamp_ip(ventana.get_rect())

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= self.tiempo_disparo:
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)
            self.ultimo_disparo = tiempo_act


class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, dueño):
        super().__init__()
        self.image_original = bala_png
        self.image = self.image_original
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = direccion
        self.velocidad = 10
        self.dueño = dueño

    def update(self):
        if self.direccion == "UP":
            self.image = pygame.transform.rotate(self.image_original, 0)
            self.rect.y -= self.velocidad
        if self.direccion == "DOWN":
            self.image = pygame.transform.rotate(self.image_original, 180)
            self.rect.y += self.velocidad
        if self.direccion == "RIGHT":
            self.image = pygame.transform.rotate(self.image_original, 270)
            self.rect.x += self.velocidad
        if self.direccion == "LEFT":
            self.image = pygame.transform.rotate(self.image_original, 90)
            self.rect.x -= self.velocidad
        if not ventana.get_rect().colliderect(self.rect):
            self.kill()


class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([ametralladora, mas_vida, escudo, velocidad_poder])
        self.rect = self.image.get_rect(center=(random.randint(50, 1300), random.randint(50, 700)))
        self.accion_poder = self.image

    def funcion_poder(self, tanque):
        if self.accion_poder == mas_vida:
            self.image = mas_vida
            if tanque.vidas < 3:
                tanque.vidas += 1
        if self.accion_poder == velocidad_poder:
            self.image = velocidad_poder
            if tanque.velocidad <= 3:
                tanque.velocidad = 6
                tanque.tiempo_velocidad = pygame.time.get_ticks()
        if self.accion_poder == ametralladora:
            self.image = ametralladora
            if tanque.tiempo_disparo >= 500:
                tanque.tiempo_disparo = 200
                tanque.tiempo_velocidad_disparo = pygame.time.get_ticks()
        if self.accion_poder == escudo:
            self.image = escudo
            tanque.escudo = True
            tanque.tiempo_escudo = pygame.time.get_ticks()



class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = random.choice([arbol_seco, arbusto_vertical, roca, tree])
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.clamp_ip(ventana.get_rect())


def reiniciar_juego():
    pygame.mixer.music.play(-1, 0.5)
    global tanque_1, tanque_2, grup_tanque, balas, poderes, obstaculos_group
    global ganador, juego_terminado, ultimo_tiempo_poder, tiempo_inicio
    tanque_1 = Tanque_p1(0, random.randint(0, 786))
    tanque_2 = Tanque_p2(1316, random.randint(0, 786))
    grup_tanque = pygame.sprite.Group(tanque_1, tanque_2)
    balas = pygame.sprite.Group()
    poderes = pygame.sprite.Group()
    obstaculos_group = pygame.sprite.Group()

    while len(obstaculos_group) < 15:
        x = random.randint(93, 907)
        y = random.randint(0, 700)
        nuevo_obstaculo = Obstaculos(x, y)
        if not pygame.sprite.spritecollideany(nuevo_obstaculo, obstaculos_group):
            obstaculos_group.add(nuevo_obstaculo)

    ganador = None
    juego_terminado = False
    ultimo_tiempo_poder = 0
    tiempo_inicio = pygame.time.get_ticks()


reiniciar_juego()

clock = pygame.time.Clock()
jugando = True

while jugando:
    clock.tick(60)
    tiempo_actual = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if juego_terminado and event.key == pygame.K_r:
                reiniciar_juego()

    if tiempo_actual - tiempo_inicio < 3000:
        ventana.fill((0, 0, 0))
        ventana.blit(fuente_arial_name.render("Shotank", True, (255, 255, 255)), (300, 50))
        ventana.blit(fuente_arial_integrantes.render("Nicolás Alfonso Cabrera Suárez", True, (255, 255, 255)), (360, 170))
        ventana.blit(fuente_arial_integrantes.render("Daniel Alejandro Rios Rincon", True, (255, 255, 255)), (370, 200))
        ventana.blit(fuente_arial_integrantes.render("Daniel Felipe Diaz Fontecha", True, (255, 255, 255)), (375, 230))
        ventana.blit(logo, (250, 300))
    else:
        ventana.fill((0, 100, 0))
        ventana.blit(vida, (0,0))
        ventana.blit(fuente_arial_integrantes.render(f"X{tanque_1.vidas}", True, (255, 255, 255)), (35,2))
        ventana.blit(vida, (935,0))
        ventana.blit(fuente_arial_integrantes.render(f"X{tanque_2.vidas}", True, (255, 255, 255)), (970, 2))
        if len(poderes) == 0 and tiempo_actual - ultimo_tiempo_poder > 15000:
            nuevo_poder = Power()
            poderes.add(nuevo_poder)
            ultimo_tiempo_poder = tiempo_actual
        if not juego_terminado:
            grup_tanque.update()
            balas.update()
            grup_tanque.draw(ventana)
            balas.draw(ventana)
            poderes.draw(ventana)
            obstaculos_group.update()
            obstaculos_group.draw(ventana)
            for bala in balas:
                if bala.dueño != tanque_1 and bala.rect.colliderect(tanque_1.rect):
                    if tanque_1.escudo:
                        colicion_bala.play()
                        bala.kill()
                        tanque_1.escudo = False
                    else:
                        colicion_bala.play()
                        tanque_1.vidas -= 1
                        bala.kill()
                        if tanque_1.vidas <= 0:
                            tanque_1.kill()
                            ganador = "Tanque 2"
                            juego_terminado = True
                if bala.dueño != tanque_2 and bala.rect.colliderect(tanque_2.rect):
                    if tanque_2.escudo:
                        colicion_bala.play()
                        bala.kill()
                        tanque_2.escudo = False
                    else:
                        colicion_bala.play()
                        tanque_2.vidas -= 1
                        bala.kill()
                        if tanque_2.vidas <= 0:
                            tanque_2.kill()
                            ganador = "Tanque 1"
                            juego_terminado = True
            for bala in balas:
                for obstaculo in obstaculos_group:
                    if bala.rect.colliderect(obstaculo.rect):
                        colicion_bala.play()
                        bala.kill()
            for tanque in grup_tanque:
                for power in poderes:
                    if tanque.rect.colliderect(power.rect):
                        powerUP.play()
                        power.funcion_poder(tanque)
                        poderes.remove(power)

            for obstaculo in obstaculos_group:
                for power in poderes:
                    if obstaculo.rect.colliderect(power.rect):
                        power.kill()
        else:
            ventana.fill((0, 0, 0))
            ventana.blit(fuente_arial_name.render("Fin del juego", True, (255, 255, 255)), (200, 200))
            ventana.blit(fuente_arial_ganador.render(f"{ganador} es el ganador", True, (255, 255, 255)), (220, 330))
            ventana.blit(fuente_arial_integrantes.render("Presiona R para reiniciar", True, (19, 161, 14)), (360, 450))

    pygame.display.flip()