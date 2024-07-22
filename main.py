import random
import pygame

"""

GAOLS!!!:
1. simple text display
2. 8x8 grid
3. use two numbers to get each square i.e. 4,6
4. flag mode

"""

bombs_count = int(input("How much many bombs"))
bombs = []
squares = []

for i in range(8):
    squares.append([])
    for j in range(8):
        squares[i].append(j+i*8)

for i in range(bombs_count):
    a = random.randrange(0, 8)
    b = random.randrange(0, 8)
    bombs.append([])
    bombs[i].append(a)
    bombs[i].append(b)
    squares[a].pop(b)

print(squares, bombs)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("minesweeper")

FPS = 60
BACKGROUND = (50, 50, 60)

def draw():
    WIN.fill(BACKGROUND)
    pygame.display.flip()

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw()


if __name__ == "__main__":
    main()