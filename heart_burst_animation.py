import pygame
import random
import math

class HeartParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(10, 30)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(3, 7)
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        self.color = random.choice([
            (255, 0, 0),      # Red
            (255, 105, 180),  # Hot pink
            (255, 20, 147),   # Deep pink
            (255, 192, 203),  # Light pink
            (255, 69, 0),     # Red-orange
        ])
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-5, 5)
        self.time_alive = 0
        self.max_time = random.uniform(1, 2)
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rotation += self.rotation_speed
        self.time_alive += 0.016
        return self.time_alive < self.max_time
        
    def draw(self, screen):
        # Create heart surface
        surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        
        # Draw heart
        center_x = self.size
        center_y = self.size
        
        # Main heart shape
        points = [
            (center_x, center_y + self.size//3),
            (center_x - self.size//2, center_y - self.size//4),
            (center_x, center_y - self.size),
            (center_x + self.size//2, center_y - self.size//4),
        ]
        
        pygame.draw.polygon(surface, self.color, points)
        pygame.draw.circle(surface, self.color, 
                         (center_x - self.size//4, center_y - self.size//4), 
                         self.size//4)
        pygame.draw.circle(surface, self.color, 
                         (center_x + self.size//4, center_y - self.size//4), 
                         self.size//4)
        
        # Rotate heart
        rotated = pygame.transform.rotate(surface, self.rotation)
        
        # Add fade out effect
        if self.time_alive > self.max_time - 0.3:
            alpha = int(255 * (self.max_time - self.time_alive) / 0.3)
            rotated.set_alpha(alpha)
            
        # Draw heart
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(rotated, rect)

class HeartBurstAnimation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []
        self.active = False
        
    def start(self, x, y):
        self.active = True
        self.particles = []
        # Create initial burst of hearts
        for _ in range(50):  # Create lots of hearts!
            self.particles.append(HeartParticle(x, y))
        
    def update(self):
        if not self.active:
            return
            
        # Update existing particles
        self.particles = [p for p in self.particles if p.update()]
        
        # Stop if no particles left
        if len(self.particles) == 0:
            self.active = False
            
    def draw(self, screen):
        if not self.active:
            return
            
        for particle in self.particles:
            particle.draw(screen)
