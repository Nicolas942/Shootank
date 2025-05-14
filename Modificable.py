import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # esto abre la pantalla con una constante 
pygame.display.set_caption("Carrera de Cuadritos")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Jugador
player_size = 40
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Enemigos 
enemy_size = 40
enemy_speed = 20
enemies = [
    [random.randint(0, WIDTH - enemy_size), 0],
    [random.randint(0, WIDTH - enemy_size), -HEIGHT // 2],
    [random.randint(0, WIDTH - enemy_size), -HEIGHT // 3],
    [random.randint(0, WIDTH - enemy_size), -HEIGHT // 4]
]

clock = pygame.time.Clock()

# Función de colisión
def detect_collision(p1, p2):
    return (
        p1[0] < p2[0] + enemy_size and
        p1[0] + player_size > p2[0] and 
        p1[1] < p2[1] + enemy_size and
        p1[1] + player_size > p2[1]
    )

# Bucle principal
running = True
while running:
    clock.tick(30)
    screen.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Movimiento enemigos
    for i in range(len(enemies)):
        enemies[i][1] += enemy_speed
        if enemies[i][1] > HEIGHT:
            enemies[i] = [random.randint(0, WIDTH - enemy_size), 0]

        # Detección de colisiones
        if detect_collision(player_pos, enemies[i]): # al colisionar con un cuadrito enemigo en la terminal aparece "Game Over"
            print("¡Game Over!")
            running = False

        # Dibujar enemigos
        pygame.draw.rect(screen, RED, (*enemies[i], enemy_size, enemy_size))

    # Dibujar jugador
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))

    pygame.display.flip()

pygame.quit()
sys.exit()
