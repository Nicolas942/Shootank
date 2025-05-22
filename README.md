# Shotank

Shotank es un juego local para dos jugadores donde cada uno controla un tanque con el objetivo de eliminar al oponente. El entorno incluye obstáculos, poderes aleatorios y mecánicas que incentivan el enfrentamiento directo en un escenario dinámico.

## Descripción General

- **Nombre del juego:** Shotank
- **Jugadores:** 2 (modo local)
- **Género:** Arcade / Shooter
- **Estilo visual:** Gráficos pixelados tipo sprite con colores llamativos.
- **Resolución:** Pantalla completa y redimensionable.

## Objetivo

El objetivo del juego es simple: destruir al tanque enemigo reduciendo sus vidas a cero mediante disparos, mientras se esquivan obstáculos y se recolectan poderes que pueden dar ventaja táctica.

## Controles

### Jugador 1 (Tanque morado)
- **Moverse:** Flechas del teclado (↑ ↓ ← →)
- **Disparar:** Tecla Enter del teclado numérico

### Jugador 2 (Tanque Naranja)
- **Moverse:** Teclas W (arriba), A (izquierda), S (abajo), D (derecha)
- **Disparar:** Barra espaciadora

## Mecánicas del Juego

### Movimiento
Cada tanque puede moverse en 4 direcciones. La rotación del sprite del tanque cambia según la dirección del movimiento.

### Disparos
- Cada tanque puede disparar en línea recta en la dirección actual.
- Existe un tiempo de recarga entre disparos.
- Los disparos se destruyen al chocar con un obstáculo o al salir de la pantalla.

### Vidas
Cada tanque comienza con **3 vidas**.
- Si un disparo enemigo impacta y el tanque no tiene escudo, pierde una vida.
- Al perder todas las vidas, el tanque es destruido y el otro jugador gana.

### Obstáculos
- Aleatorios en cada partida.
- Impiden el movimiento de los tanques y bloquean disparos.

### Poderes
Cada cierto tiempo aparece un poder aleatorio en el campo de batalla. Tipos de poder:
- **Más vida:** Añade una vida extra (máximo 3).
- **Velocidad:** Aumenta la velocidad del tanque por 10 segundos.
- **Metralleta:** Reduce el tiempo entre disparos por 5 segundos.
- **Escudo:** Absorbe un disparo recibido. Dura 10 segundos o hasta recibir impacto.

## Interfaz

- Se muestra el nombre del juego y los nombres de los integrantes al inicio.
- En pantalla se muestran las vidas restantes de cada jugador con íconos de corazón.
- Al finalizar, se muestra una pantalla con el ganador y opción de reinicio (`R`).

## Créditos

- **Desarrolladores:**
  - Nicolás Alfonso Cabrera Suárez
  - Daniel Alejandro Ríos Rincón
  - Daniel Felipe Díaz Fontecha

## Cómo Reiniciar

- Al finalizar una partida, presiona la tecla `R` para reiniciar el juego.

## Cómo Salir

- Presiona `ESC` en cualquier momento para cerrar el juego.

---



