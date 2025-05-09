import pygame, sys, random  # Importación de las librerías necesarias

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana del juego en pantalla completa y redimensionable
ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)

# Definición de fuentes de texto para el título y nombres de los integrantes
fuente_arial_name = pygame.font.SysFont("arial", 100, 1, 1)
fuente_arial_integrantes = pygame.font.SysFont("arial", 20, 1, 1)
fuente_arial_ganador = pygame.font.SysFont("arial", 50, 1, 1)

# Clase del tanque controlado por el jugador 1
class Tanque_p1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Crea una superficie cuadrada de 50x50 px
        self.image.fill((255, 0, 0))  # Rellena el tanque con color rojo
        self.rect = self.image.get_rect(center=(x, y))  # Establece la posición inicial
        self.direccion = "UP"  # Dirección inicial del tanque
        self.vidas = 5  # Número de vidas del tanque
        self.ultimo_disparo = 0  # Tiempo del último disparo

    def update(self):
        teclas = pygame.key.get_pressed()  # Detecta las teclas presionadas
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
            self.disparar(balas)  # Dispara una bala si se presiona Enter del teclado numérico
        self.rect.clamp_ip(ventana.get_rect())  # Limita el movimiento dentro de la pantalla

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks()  # Obtiene el tiempo actual
        if tiempo_act - self.ultimo_disparo >= 500:  # Dispara si han pasado al menos 500ms
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)
            self.ultimo_disparo = tiempo_act  # Actualiza el tiempo del último disparo

# Clase del tanque controlado por el jugador 2
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
            self.disparar(balas)  # Dispara una bala si se presiona la barra espaciadora
        self.rect.clamp_ip(ventana.get_rect())

    def disparar(self, balas):
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= 500:
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)
            self.ultimo_disparo = tiempo_act

# Clase para las balas disparadas por los tanques
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, dueño):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Tamaño de la bala
        self.image.fill((0, 0, 255))  # Color azul para la bala
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = direccion
        self.velocidad = 10  # Velocidad de desplazamiento
        self.dueño = dueño  # Referencia al tanque que disparó la bala

    def update(self):
        # Movimiento según la dirección
        if self.direccion == "UP":
            self.rect.y -= self.velocidad
        if self.direccion == "DOWN":
            self.rect.y += self.velocidad
        if self.direccion == "RIGHT":
            self.rect.x += self.velocidad
        if self.direccion == "LEFT":
            self.rect.x -= self.velocidad
        if not ventana.get_rect().colliderect(self.rect):  # Elimina la bala si sale de la pantalla
            self.kill()

# Crear tanques con sus posiciones iniciales
tanque_1 = Tanque_p1(0, random.randint(0,780))
tanque_2 = Tanque_p2(1366, random.randint(0,780))

# Grupos de sprites para los tanques y las balas
grup_tanque = pygame.sprite.Group(tanque_1, tanque_2)
balas = pygame.sprite.Group()

# Reloj para controlar la tasa de actualización del juego (FPS)
clock = pygame.time.Clock()

# Variables para control de juego
jugando = True
ganador = None
juego_terminado = False

# Bucle principal del juego
while jugando:
    clock.tick(60)
    crono = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    # Pantalla de inicio
    if crono < 3000:
        ventana.fill((0, 0, 0))
        ventana.blit(fuente_arial_name.render(f"Shotank", True, (255,255,255)), (480,50))
        ventana.blit(fuente_arial_integrantes.render(f"Nicolás Alfonso Cabrera Suárez", True,  (255,255,255)), (525, 170) )
        ventana.blit(fuente_arial_integrantes.render(f"Daniel Alejandro Rios Rincon", True,  (255,255,255)), (535, 200) )
        ventana.blit(fuente_arial_integrantes.render(f"Daniel Felipe Diaz Fontecha", True,  (255,255,255)), (540, 230) )

        
    else: # Se inicia el juego principal
        ventana.fill((0, 255, 0))

        if not juego_terminado:
            grup_tanque.update()
            balas.update()
            grup_tanque.draw(ventana)
            balas.draw(ventana)

            for bala in balas:
                if bala.dueño != tanque_1 and bala.rect.colliderect(tanque_1.rect): #verifica los impactos al tanque 1
                    tanque_1.vidas -= 1 # resta vida al tanque 1
                    bala.kill() # elimina la bala tras el impacto
                    if tanque_1.vidas <= 0: # Comprueba si quedan vidas
                        tanque_1.kill() # elimina el tanque si no tiene vidas
                        ganador = "Tanque 2" # establece El ganador 
                        juego_terminado = True # pausa el juego

                if bala.dueño != tanque_2 and bala.rect.colliderect(tanque_2.rect): #verifica los impactos al tanque 2
                    tanque_2.vidas -= 1 # resta vida al tanque 2
                    bala.kill() # elimina la bala tras el impacto
                    if tanque_2.vidas <= 0: # Comprueba si quedan vidas
                        tanque_2.kill() # elimina el tanque si no tiene vidas
                        ganador = "Tanque 1" # establece El ganador 
                        juego_terminado = True # pausa el juego

        else: #inicia la pantalla final 
            ventana.fill((0, 0, 0))
            ventana.blit(fuente_arial_name.render("Fin del juego", True, (255, 255, 255)), (340, 200))
            ventana.blit(fuente_arial_ganador.render(f"{ganador} es el ganador", True, (255, 255, 255)), (360, 330))

    pygame.display.flip()
