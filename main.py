import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Initialize pygame module
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Initialize clock and delta time control
    clock = pygame.time.Clock()
    dt = 0
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    # Create instance of player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Create instance of asteroids field to allocate asteroids
    asteroid_field = AsteroidField()
    
    
    # Main inf loop
    while True:
        # Log game state data to game_state.jsonl
        log_state()
        
        for event in pygame.event.get():
            # Allows exiting game on window closing
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        # Update game state
        updatable.update(dt)
        # Draw game objects on screen
        for object in drawable:
            object.draw(screen)
        
        
        # Refresh screen
        pygame.display.flip()
        
        # Wait until 1/60 of a second has passed and register time since last call
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
