import pygame
import numpy as np

# Configuración de colores
BG_COLOR = (10, 10, 10)
GRID_COLOR = (40, 40, 40)
CELL_COLOR = (255, 255, 255)
TEXT_COLOR = (200, 200, 200)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Conway - HelloMath")

# Fuente para texto
font = pygame.font.Font(None, 36)

def draw_text(text, pos):
    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, pos)

def get_board_dimensions():
    selecting = True
    dimensions = None
    while selecting:
        screen.fill(BG_COLOR)
        draw_text("Selecciona el tamaño del tablero:", (50, 50))
        draw_text("1. 9x9", (50, 100))
        draw_text("2. 16x5", (50, 150))


        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    dimensions = (9, 9)
                    selecting = False
                elif event.key == pygame.K_2:
                    dimensions = (16, 5)
                    selecting = False


    return dimensions

def main():
    nx, ny = get_board_dimensions()
    cell_size = 80  # Tamaño fijo de celda para todos los tableros
    width, height = nx * cell_size, ny * cell_size

    screen = pygame.display.set_mode((width, height))
    board = np.zeros((nx, ny))
    history = [np.copy(board)]

    def draw_grid():
        for x in range(0, width, cell_size):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, height))
        for y in range(0, height, cell_size):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (width, y))

    def draw_cells():
        for x in range(nx):
            for y in range(ny):
                if board[x, y] == 1:
                    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size - 1, cell_size - 1)
                    pygame.draw.rect(screen, CELL_COLOR, rect)

    def update_board():
        nonlocal board  # Use nonlocal to modify the board variable from the enclosing scope
        new_board = np.copy(board)
        for x in range(nx):
            for y in range(ny):
                neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if 0 <= x + i < nx and 0 <= y + j < ny:
                            neighbors += board[x + i, y + j]

                if board[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                    new_board[x, y] = 0
                elif board[x, y] == 0 and neighbors == 3:
                    new_board[x, y] = 1
        board = new_board

    running = True
    paused = True  # Empezar en estado pausado para permitir la configuración inicial
    clock = pygame.time.Clock()
    history_index = 0

    while running:
        screen.fill(BG_COLOR)
        draw_grid()
        draw_cells()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    board = np.zeros((nx, ny))  # Resetear tablero
                    history = [np.copy(board)]  # Resetear historial
                    history_index = 0
                    paused = True  # Pausar después del reset
                elif event.key == pygame.K_n:  # Avanzar un estado manualmente
                    if paused:
                        update_board()
                        history.append(np.copy(board))
                        history_index += 1
                elif event.key == pygame.K_b:  # Retroceder al estado anterior
                    if paused and history_index > 0:
                        history_index -= 1
                        board = np.copy(history[history_index])
            elif event.type == pygame.MOUSEBUTTONDOWN and paused:
                x, y = pygame.mouse.get_pos()
                x //= cell_size
                y //= cell_size
                board[x, y] = not board[x, y]  # Cambiar el estado de la celda

        if not paused:
            update_board()
            history.append(np.copy(board))
            history_index += 1

        pygame.display.flip()
        clock.tick(10)  # FPS

    pygame.quit()

if __name__ == "__main__":
    main()
