import pygame
import random
import math

class MagnifyingGlassParticle:
    def __init__(self, width, height):
        # Random starting position around the edges
        side = random.randint(0, 3)
        if side == 0:  # Top
            self.x = random.randint(0, width)
            self.y = -50
        elif side == 1:  # Right
            self.x = width + 50
            self.y = random.randint(0, height)
        elif side == 2:  # Bottom
            self.x = random.randint(0, width)
            self.y = height + 50
        else:  # Left
            self.x = -50
            self.y = random.randint(0, height)
            
        self.width = width
        self.height = height
        self.size = random.randint(30, 40)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 4)
        
        # Calculate direction towards center
        center_x = width // 2
        center_y = height // 2
        dx = center_x - self.x
        dy = center_y - self.y
        length = math.sqrt(dx * dx + dy * dy)
        self.dx = (dx / length) * self.speed
        self.dy = (dy / length) * self.speed
        
        self.rotation = 0
        self.rotation_speed = random.uniform(-3, 3)
        self.time_alive = 0
        self.max_time = random.uniform(3, 5)  # Live for 3-5 seconds
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rotation += self.rotation_speed
        self.time_alive += 0.016  # Approximately 60 FPS
        
        # Return True while particle is alive
        return self.time_alive < self.max_time
        
    def draw(self, screen):
        # Create surface for magnifying glass
        surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        
        # Draw handle
        handle_color = (139, 69, 19)  # Brown
        handle_start = (self.size * 0.7, self.size * 0.7)
        handle_end = (self.size * 0.9, self.size * 0.9)
        pygame.draw.line(surface, handle_color, handle_start, handle_end, 4)
        
        # Draw glass circle
        glass_color = (200, 200, 255, 150)  # Light blue, semi-transparent
        glass_pos = (int(self.size * 0.4), int(self.size * 0.4))
        glass_radius = int(self.size * 0.3)
        pygame.draw.circle(surface, glass_color, glass_pos, glass_radius)
        
        # Draw rim
        rim_color = (100, 100, 100)  # Gray
        pygame.draw.circle(surface, rim_color, glass_pos, glass_radius, 2)
        
        # Draw heart in the glass
        heart_color = (255, 192, 203)  # Pink
        heart_size = glass_radius // 2
        heart_pos = (glass_pos[0], glass_pos[1])
        self.draw_heart(surface, heart_pos, heart_size, heart_color)
        
        # Rotate the surface
        rotated = pygame.transform.rotate(surface, self.rotation)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        
        # Draw with fade out near end of life
        if self.time_alive > self.max_time - 0.5:
            alpha = int(255 * (self.max_time - self.time_alive) * 2)
            rotated.set_alpha(alpha)
        screen.blit(rotated, rect)
        
    def draw_heart(self, surface, pos, size, color):
        x, y = pos
        points = [
            (x, y + size//3),
            (x - size//2, y - size//4),
            (x, y - size),
            (x + size//2, y - size//4),
        ]
        pygame.draw.polygon(surface, color, points)
        pygame.draw.circle(surface, color, (x - size//4, y - size//4), size//4)
        pygame.draw.circle(surface, color, (x + size//4, y - size//4), size//4)

class MagnifyingGlassAnimation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []
        self.active = False
        self.spawn_timer = 0
        
    def start(self):
        self.active = True
        self.particles = []
        # Create initial burst of magnifying glasses
        for _ in range(30):  # Increased from default
            self.particles.append(MagnifyingGlassParticle(self.width, self.height))
        self.spawn_timer = 0
        
    def update(self):
        if not self.active:
            return
            
        # Spawn new particles more frequently
        self.spawn_timer += 1
        if self.spawn_timer >= 10:  # Reduced from 20 to 10 for more frequent spawning
            # Spawn multiple particles at once
            for _ in range(3):  # Spawn 3 particles at a time
                self.particles.append(MagnifyingGlassParticle(self.width, self.height))
            self.spawn_timer = 0
            
        # Update existing particles
        self.particles = [p for p in self.particles if p.update()]
        
        # Stop if no particles and not recently started
        if len(self.particles) == 0 and self.spawn_timer > 60:
            self.active = False
            
    def draw(self, screen):
        if not self.active:
            return
            
        for particle in self.particles:
            particle.draw(screen)
