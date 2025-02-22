import pygame
import player
from constants import *



def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygameClock = pygame.time.Clock()

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    current_player = player.Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        current_player.draw(screen)
        pygame.display.flip()
        dt = pygameClock.tick(60) / 1000

        current_player.update(dt)

    """
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    """



if __name__ == "__main__":
    main()