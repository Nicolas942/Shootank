import pygame

# Inicializar Pygame
pygame.init()

# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
TILE_SIZE = 32
BLOCK_SIZE = 96
GRID_ROWS = SCREEN_HEIGHT // TILE_SIZE
GRID_COLS = SCREEN_WIDTH // TILE_SIZE

# Colores
BLACK = (0, 0, 0)
GRASS_COLOR = (34, 139, 34)
GRAY_COLOR = (120, 120, 120)  # Color gris para todos los bloques

# Inicializar pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escenario con 6 bloques grises fijos")

# Dibujar fondo de pasto
def draw_grass_background():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            pygame.draw.rect(screen, GRASS_COLOR, (x, y, TILE_SIZE, TILE_SIZE))

# Dibujar bloques grises en posiciones fijas
def draw_gray_blocks():
    block_positions = [
        (50, 100),
        (300, 70),
        (100, 320),
        (500, 150),
        (200, 550),
        (400, 380),
    ]

    for x, y in block_positions:
        pygame.draw.rect(screen, GRAY_COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE))

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    draw_grass_background()
    draw_gray_blocks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
