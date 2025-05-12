import pygame,sys,random

#inicializar los modulos de pygame

pygame.init()

# Definir la ventana
ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)

#Fuentes de texto a utilizar
fuente_arial_name = pygame.font.SysFont("arial", 100, 1, 1)
fuente_arial_integrantes = pygame.font.SysFont("arial", 20, 1, 1)
fuente_arial_ganador = pygame.font.SysFont("arial", 50, 1, 1)

#clase del tanque 1
class Tanque_p1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50)) # superficie del tanque
        self.image.fill((255, 0, 0)) # Color rojo para el tanque 
        self.rect = self.image.get_rect(center=(x, y)) # centro del tanque
        self.direccion = "UP" # direccion del tanque
        self.velocidad = 3
        self.vidas = 3# Numero de vidas
        self.ultimo_disparo = 0 # Tiempo del ultio disparo
        self.tiempo_velocidad = 0
        self.tiempo_disparo = 500
        self.tiempo_velocidad_disparo = 0

    def update(self):
        #teclas de moviento
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
            self.direccion = "UP"
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad
            self.direccion = "DOWN"
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
            self.direccion = "RIGHT"
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
            self.direccion = "LEFT"
        if teclas[pygame.K_KP_ENTER]:
            self.disparar(balas)

        if self.velocidad > 3 and pygame.time.get_ticks() - self.tiempo_velocidad > 10000:
            self.velocidad = 3
        if self.tiempo_disparo <= 500 and pygame.time.get_ticks() - self.tiempo_velocidad_disparo > 5000:
            self.tiempo_disparo = 500
        # el tanque no puede salir de la ventana
        self.rect.clamp_ip(ventana.get_rect())

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks() # tiempo de juego
        if tiempo_act - self.ultimo_disparo >= self.tiempo_disparo: #establece un intervalo 
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self) # posicion de la bala
            balas.add(bala) #Agregar una bala a la lista de balas
            self.ultimo_disparo = tiempo_act #reinicia el intervalo

#tanque 2
class Tanque_p2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = "UP"
        self.velocidad = 3
        self.vidas = 3
        self.ultimo_disparo = 0
        self.tiempo_velocidad = 0
        self.tiempo_disparo = 500
        self.tiempo_velocidad_disparo = 0


    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            self.rect.y -= self.velocidad
            self.direccion = "UP"
        if teclas[pygame.K_s]:
            self.rect.y += self.velocidad
            self.direccion = "DOWN"
        if teclas[pygame.K_d]:
            self.rect.x += self.velocidad
            self.direccion = "RIGHT"
        if teclas[pygame.K_a]:
            self.rect.x -= self.velocidad
            self.direccion = "LEFT"
        if teclas[pygame.K_SPACE]:
            self.disparar(balas)
        self.rect.clamp_ip(ventana.get_rect())

        if self.velocidad > 3 and pygame.time.get_ticks() - self.tiempo_velocidad > 10000:
            self.velocidad = 3
        if self.tiempo_disparo <= 500 and pygame.time.get_ticks() - self.tiempo_velocidad_disparo > 5000:
            self.tiempo_disparo = 500

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= self.tiempo_disparo:
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)
            self.ultimo_disparo = tiempo_act

# Calse bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, dueño):
        super().__init__()
        self.image = pygame.Surface((20, 20)) #dimenciones de la bala
        self.image.fill((0, 0, 255)) # color azul de la bala
        self.rect = self.image.get_rect(center=(x, y)) #ubicacion de la bala
        self.direccion = direccion # direccion de la bala
        self.velocidad = 10 # Velocidad de la bala
        self.dueño = dueño #dueño daño de la bala

    def update(self):
        if self.direccion == "UP":
            self.rect.y -= self.velocidad
        if self.direccion == "DOWN":
            self.rect.y += self.velocidad
        if self.direccion == "RIGHT":
            self.rect.x += self.velocidad
        if self.direccion == "LEFT":
            self.rect.x -= self.velocidad
        # la bala se borra de la lista balas si sale de la ventana
        if not ventana.get_rect().colliderect(self.rect):
            self.kill()

#clase poder
class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15)) #tamaño del poder
        self.image.fill((0, 0, 0)) # color negro del poder
        self.rect = self.image.get_rect(center=(random.randint(50, 1300), random.randint(50, 700))) #ubicacion aleatoria del poder
        self.accion_poder = random.choice(["más_vida", "velocidad", "metralleta", "escudo"])

    def funcion_poder(self, tanque):
        if self.accion_poder == "más_vida":
            if tanque.vidas < 3:
             tanque.vidas += 1
        if self.accion_poder == "velocidad":
            if tanque.velocidad <= 3:
                tanque.velocidad = 6
                tanque.tiempo_velocidad = pygame.time.get_ticks()
        if self.accion_poder == "metralleta":
            if tanque.tiempo_disparo >= 500:
                tanque.tiempo_disparo = 200
                tanque.tiempo_velocidad_disparo = pygame.time.get_ticks()



       


class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill((22, 22, 22))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.clamp_ip(ventana.get_rect())


tanque_1 = Tanque_p1(0, random.randint(0, 780)) # se crea el tanque 1
tanque_2 = Tanque_p2(1366, random.randint(0, 780)) # se crea el tanque 2

grup_tanque = pygame.sprite.Group(tanque_1, tanque_2) #se forma un grupo cin el tanque 1 y 2
balas = pygame.sprite.Group() #grupo de balas
poderes = pygame.sprite.Group() # grupo de poderes
obstaculos_group = pygame.sprite.Group()

for _ in range(10):
    x = random.randint(60, 1306)
    y = random.randint(0, 786)
    obstaculo = Obstaculos(x, y)
    obstaculos_group.add(obstaculo)

clock = pygame.time.Clock() #control de fps
jugando = True # es Jueo se activa
ganador = None # espera a saber quien es el ganador 
juego_terminado = False # pausa el juego
ultimo_tiempo_poder = 0 # ultima vez que se uso un poder 

#Bucle principal

while jugando:
    clock.tick(60) # número de FPS
    tiempo_actual = pygame.time.get_ticks() #Tiempo actual

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    #Pantalla de inicio

    if tiempo_actual < 3000:
        ventana.fill((0, 0, 0))
        ventana.blit(fuente_arial_name.render("Shotank", True, (255, 255, 255)), (480, 50))
        ventana.blit(fuente_arial_integrantes.render("Nicolás Alfonso Cabrera Suárez", True, (255, 255, 255)), (525, 170))
        ventana.blit(fuente_arial_integrantes.render("Daniel Alejandro Rios Rincon", True, (255, 255, 255)), (535, 200))
        ventana.blit(fuente_arial_integrantes.render("Daniel Felipe Diaz Fontecha", True, (255, 255, 255)), (540, 230))
    else: #inicio del juego
        ventana.fill((0, 255, 0))

        # Generar un poder solo si no hay otro
        if len(poderes) == 0 and tiempo_actual - ultimo_tiempo_poder > 5000:
            nuevo_poder = Power()
            poderes.add(nuevo_poder)
            ultimo_tiempo_poder = tiempo_actual
            # se cargan las clases 
        if not juego_terminado:
            grup_tanque.update()
            balas.update()
            grup_tanque.draw(ventana)
            balas.draw(ventana)
            poderes.draw(ventana)
            obstaculos_group.update()
            obstaculos_group.draw(ventana)
            
            # Se verifican las coliciones 
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

            for bala in balas:
                for obstaculo in obstaculos_group:
                    if bala.rect.colliderect(obstaculo.rect):
                        bala.kill()

            for tanque in grup_tanque:
                for obstaculo in obstaculos_group:
                    if tanque.direccion == "UP" and tanque.rect.colliderect(obstaculo.rect):
                        tanque.rect.y += 1.5
                    if tanque.direccion == "DOWN" and tanque.rect.colliderect(obstaculo.rect):
                        tanque.rect.y -= 1.5
                    if tanque.direccion == "LEFT" and tanque.rect.colliderect(obstaculo.rect):
                        tanque.rect.x += 1.5
                    if tanque.direccion == "RIGHT" and tanque.rect.colliderect(obstaculo.rect):
                        tanque.rect.x -= 1.5

            # Recoger poder 
            for tanque in grup_tanque:
                for power in poderes:
                    if tanque.rect.colliderect(power.rect):
                        power.funcion_poder(tanque)
                        poderes.remove(power)
                        
        else: #pantalla final
            ventana.fill((0, 0, 0))
            ventana.blit(fuente_arial_name.render("Fin del juego", True, (255, 255, 255)), (340, 200))
            ventana.blit(fuente_arial_ganador.render(f"{ganador} es el ganador", True, (255, 255, 255)), (360, 330))

    pygame.display.flip() # actualiza la pantalla




