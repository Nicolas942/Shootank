import pygame, sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana del juego
ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)

# Clase del tanque controlado por el jugador 1
class Tanque_p1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Representación gráfica del tanque
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Color rojo para el tanque
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = "UP"  # Dirección inicial del tanque
        self.vidas = 5  # Número de vidas iniciales del tanque
        self.ultimo_disparo = 0  # Control de tiempo del último disparo

    def update(self):
        # Teclas presionadas
        teclas = pygame.key.get_pressed()

        # Movimiento del tanque
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

        # Disparo con la tecla ENTER del teclado numérico
        if teclas[pygame.K_KP_ENTER]:
            tanque_1.disparar(balas)

        # Restringe el movimiento del tanque dentro del área de la ventana
        self.rect.clamp_ip(ventana.get_rect())

    def disparar(self, balas):
        # Control de tiempo para limitar la frecuencia de disparos
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= 200:  # 200 ms entre disparos
            # Crea una nueva bala en la dirección actual
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)  # Agrega la bala al grupo de balas
            self.ultimo_disparo = tiempo_act


# Clase del tanque controlado por el jugador 2, hereda de Tanque_p1
class Tanque_p2(Tanque_p1, pygame.sprite.Sprite):
    def update(self):
        # Captura de las teclas presionadas para el jugador 2
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:  # Movimiento hacia arriba
            self.rect.y -= 3
            self.direccion = "UP"
        if teclas[pygame.K_s]:  # Movimiento hacia abajo
            self.rect.y += 3
            self.direccion = "DOWN"
        if teclas[pygame.K_d]:  # Movimiento hacia la derecha
            self.rect.x += 3
            self.direccion = "RIGHT"
        if teclas[pygame.K_a]:  # Movimiento hacia la izquierda
            self.rect.x -= 3
            self.direccion = "LEFT"

        # Disparo con la tecla ESPACIO
        if teclas[pygame.K_SPACE]:
            tanque_2.disparar(balas)

        # Restringe el movimiento del tanque dentro del área de la ventana
        self.rect.clamp_ip(ventana.get_rect())
    
    def disparar(self, balas):
        # Control de tiempo para limitar la frecuencia de disparos
        tiempo_act = pygame.time.get_ticks()
        if tiempo_act - self.ultimo_disparo >= 200:  # 2 segundos entre disparos
            # Crea una nueva bala en la dirección actual
            bala = Bala(self.rect.centerx, self.rect.centery, self.direccion, self)
            balas.add(bala)  # Agrega la bala al grupo de balas
            self.ultimo_disparo = tiempo_act


# Clase para las balas disparadas por los tanques
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, dueño):
        super().__init__()
        # Representación gráfica de la bala
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))  # Color azul para la bala
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = direccion  # Dirección en la que se mueve la bala
        self.velocidad = 10  # Velocidad de la bala
        self.dueño = dueño  # Tanque que disparó la bala

    def update(self):
        # Movimiento de la bala en la dirección indicada
        if self.direccion == "UP":
            self.rect.y -= self.velocidad
        if self.direccion == "DOWN":
            self.rect.y += self.velocidad
        if self.direccion == "RIGHT":
            self.rect.x += self.velocidad
        if self.direccion == "LEFT":
            self.rect.x -= self.velocidad
        
        # Elimina la bala si sale del área de la ventana
        if not ventana.get_rect().colliderect(self.rect):
            self.kill()


# Creación de instancias de los tanques
tanque_1 = Tanque_p1(0, 700)
tanque_2 = Tanque_p2(500, 700)

# Grupos de sprites para los tanques y las balas
grup_tanque = pygame.sprite.Group(tanque_1, tanque_2)
balas = pygame.sprite.Group()

# Control de FPS
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    # Configuración del límite de FPS
    clock.tick(60)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Salir del juego con ESC
                sys.exit()

    # Dibujar el fondo de la ventana
    ventana.fill((0, 255, 0))  # Color verde para el fondo

    # Actualizar y dibujar sprites
    grup_tanque.update()
    balas.update()
    grup_tanque.draw(ventana)
    balas.draw(ventana)

    # Detectar colisiones entre balas y tanques
    for bala in balas:
        if bala.dueño != tanque_1 and bala.rect.colliderect(tanque_1.rect):
            tanque_1.vidas -= 1  # Disminuir vidas del tanque 1
            bala.kill()  # Eliminar la bala
            if tanque_1.vidas <= 0:  # Evalua si el tanque tiene vidas
                tanque_1.kill() # Elimina el tanque_1
        if bala.dueño != tanque_2 and bala.rect.colliderect(tanque_2.rect):
            tanque_2.vidas -= 1  # Disminuir vidas del tanque 2
            bala.kill()  # Eliminar la bala
            if tanque_2.vidas <= 0:  # Evalua si el tanque tiene vidas
                tanque_2.kill() # Elimina el tanque_2

    # Actualizar la pantalla
    pygame.display.flip()
