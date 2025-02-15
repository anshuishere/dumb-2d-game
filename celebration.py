import pygame
import random
import math

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(4, 8)
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.lifetime = random.randint(30, 60)  # frames
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1  # gravity
        self.lifetime -= 1
        self.size = max(0, self.size - 0.1)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class Celebration:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []
        self.celebrating = False
        self.celebration_colors = [
            (255, 215, 0),   # Gold
            (255, 0, 0),     # Red
            (0, 255, 0),     # Green
            (0, 0, 255),     # Blue
            (255, 192, 203), # Pink
            (255, 165, 0)    # Orange
        ]
        
    def start(self):
        self.celebrating = True
        # Create initial burst of particles
        for _ in range(50):  # Create 50 particles
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            color = random.choice(self.celebration_colors)
            self.particles.append(Particle(x, y, color))
            
    def update(self):
        if not self.celebrating:
            return
            
        # Add new particles occasionally
        if random.random() < 0.3:  # 30% chance each frame
            x = random.randint(0, self.width)
            y = self.height + 10  # Start from bottom
            color = random.choice(self.celebration_colors)
            self.particles.append(Particle(x, y, color))
            
        # Update existing particles
        for particle in self.particles[:]:
            particle.update()
            if particle.lifetime <= 0:
                self.particles.remove(particle)
                
        # Stop celebration if no particles left
        if len(self.particles) == 0:
            self.celebrating = False
            
    def draw(self, screen):
        if not self.celebrating:
            return
            
        for particle in self.particles:
            particle.draw(screen)
