import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from player import Player


def main():
    # Initialize pygame module
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Initialize clock and delta time control
    clock = pygame.time.Clock()
    dt = 0
    
    # Main inf loop
    while True:
        # Log game state data to game_state.jsonl
        log_state()
        
        for event in pygame.event.get():
            # Allows exiting game on window closing
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        # Create instance of player and draw it on screen
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        player.draw(screen)
        
        # Refresh screen
        pygame.display.flip()
        
        # Wait until 1/60 of a second has passed and register time since last call
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
