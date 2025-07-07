import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock=pygame.time.Clock()
    dt=0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers=(updatable,drawable)
    Asteroid.containers=(updatable,drawable,asteroids)
    AsteroidField.containers=(updatable)
    Shot.containers=(updatable,drawable,shots)
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidField=AsteroidField()
    while True:
        screen.fill(pygame.Color(0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.kill()
            
        for todraw in drawable:
            todraw.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt=game_clock.tick(60)/1000

if __name__ == "__main__":
    main()
