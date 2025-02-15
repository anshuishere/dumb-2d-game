import pygame
import random
import math

class StarParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(15, 25)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 4)
        self.fall_speed = random.uniform(1, 3)
        self.oscillation_speed = random.uniform(0.05, 0.1)
        self.oscillation_width = random.uniform(30, 50)
        self.time = random.uniform(0, 2 * math.pi)
        self.color = (255, 255, 0)  # Yellow stars
        self.points = 5  # 5-pointed star
        
    def update(self):
        self.time += self.oscillation_speed
        self.x = self.x + math.sin(self.time) * self.oscillation_width * 0.1
        self.y += self.fall_speed
        return self.y < 800  # Return False when particle goes off screen

    def draw(self, screen):
        # Calculate star points
        points = []
        for i in range(self.points * 2):
            angle = (i * math.pi) / self.points
            radius = self.size if i % 2 == 0 else self.size * 0.4
            x = self.x + radius * math.cos(angle + self.time * 0.5)  # Rotate star
            y = self.y + radius * math.sin(angle + self.time * 0.5)
            points.append((x, y))
        
        # Draw star
        pygame.draw.polygon(screen, self.color, points)
        # Add glow effect
        pygame.draw.polygon(screen, (255, 255, 200), points, 2)

class StarAnimation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []
        self.active = False
        
    def start(self):
        self.active = True
        # Create initial burst of stars
        for _ in range(20):  # Create 20 stars
            x = random.randint(0, self.width)
            y = random.randint(-100, 0)  # Start above screen
            self.particles.append(StarParticle(x, y))
            
    def update(self):
        if not self.active:
            return
            
        # Add new particles occasionally
        if random.random() < 0.1:  # 10% chance each frame
            x = random.randint(0, self.width)
            self.particles.append(StarParticle(x, -20))
            
        # Update existing particles
        self.particles = [p for p in self.particles if p.update()]
        
        # Stop animation if no particles left
        if len(self.particles) == 0:
            self.active = False
            
    def draw(self, screen):
        if not self.active:
            return
            
        for particle in self.particles:
            particle.draw(screen)
