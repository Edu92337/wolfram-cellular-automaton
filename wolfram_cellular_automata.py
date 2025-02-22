import pygame
import numpy as np

WIDTH,HEIGHT = 650,650
CELL_SIZE = 10
GRID_HEIGHT = HEIGHT//CELL_SIZE
GRID_WIDTH = WIDTH//CELL_SIZE

def rule(a, b, c):
    pattern = (a << 2) | (b << 1) | c
    rule_number = 110
    return (rule_number >> pattern) & 1


def generations():
    gen = np.zeros((GRID_HEIGHT,GRID_WIDTH),dtype=int)
    gen[0][GRID_WIDTH//2] = 1
    for i in range(1, GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            left = gen[i-1][(j-1) % GRID_WIDTH]
            right = gen[i-1][(j+1) % GRID_WIDTH]
            atual = gen[i-1][j % GRID_WIDTH]
            gen[i][j] = rule(left, atual, right)
    return gen
    
def main():
    running = True
    gen0 = generations()
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    pygame.display.set_caption("Wolfram CA")
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                pygame.draw.rect(screen,'white' if (gen0[i][j] == 1) else 'black',(CELL_SIZE*j,CELL_SIZE*i,CELL_SIZE,CELL_SIZE))

        pygame.display.flip()
        dt = clock.tick(60) / 100

    pygame.quit()

if __name__ == "__main__":
    main()