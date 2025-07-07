import pygame
from constants import *
def main():
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock=pygame.time.Clock()
    dt=0
    while True:
        screen.fill((0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt=game_clock.tick(60)/1000
if __name__ == "__main__":
    main()
