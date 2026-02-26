import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_INCREASE    


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    
    # Call when asteroid is hit with a shot
    def split(self):
        # Always delete current asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            # If asteroid is big, it splits into fragments, two new asteroids are created with some extra speed
            split_angle = random.uniform(20, 50)
            first_new_velocity = self.velocity.rotate(split_angle) * ASTEROID_SPLIT_SPEED_INCREASE
            second_new_velocity = self.velocity.rotate(-split_angle) * ASTEROID_SPLIT_SPEED_INCREASE
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            first_new_asteroid.velocity = first_new_velocity
            second_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_new_asteroid.velocity = second_new_velocity
            
        
        
        
def main():
    pass      

if __name__ == "__main__":
    main()
