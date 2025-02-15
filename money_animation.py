import pygame
import random
import math

class MoneyParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.original_y = y
        self.size = random.randint(20, 30)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 4)
        self.fall_speed = random.uniform(1, 3)
        self.oscillation_speed = random.uniform(0.05, 0.1)
        self.oscillation_width = random.uniform(30, 50)
        self.time = random.uniform(0, 2 * math.pi)
        
    def update(self):
        self.time += self.oscillation_speed
        self.x = self.x + math.sin(self.time) * self.oscillation_width * 0.1
        self.y += self.fall_speed
        return self.y < 800  # Return False when particle goes off screen

    def draw(self, screen):
        # Draw a dollar sign
        font = pygame.font.Font(None, self.size)
        text = font.render("$", True, (34, 139, 34))  # Dollar sign in green
        text_rect = text.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(text, text_rect)

class MoneyAnimation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []
        self.active = False
        
    def start(self):
        self.active = True
        # Create initial burst of money
        for _ in range(30):  # Create 30 dollar signs
            x = random.randint(0, self.width)
            y = random.randint(-100, 0)  # Start above screen
            self.particles.append(MoneyParticle(x, y))
            
    def update(self):
        if not self.active:
            return
            
        # Add new particles occasionally
        if random.random() < 0.1:  # 10% chance each frame
            x = random.randint(0, self.width)
            self.particles.append(MoneyParticle(x, -20))
            
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
