import pygame
import math
import random

class CorbettBackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.target_reached = False
        self.wedding_stage_x = width - 200
        self.wedding_stage_y = height - 100
        self.tiger_positions = []
        self.initialize_tigers()
        
    def initialize_tigers(self):
        # Create 3 tigers at random positions in the background
        for _ in range(3):
            x = random.randint(200, self.width - 300)
            y = self.height - 120  # Tigers on ground level
            direction = random.choice([-1, 1])  # -1 for left, 1 for right
            self.tiger_positions.append([x, y, direction])
    
    def draw(self, screen):
        # Sunset gradient sky
        for i in range(self.height):
            # Create a sunset gradient from orange to dark blue
            factor = i / self.height
            r = int(255 * (1 - factor * 0.7))  # More orange at bottom
            g = int(100 * (1 - factor))        # Less green for sunset
            b = int(50 + factor * 150)         # More blue at top
            pygame.draw.line(screen, (r, g, b), (0, i), (self.width, i))
        
        # Add "Jim Corbett National Park" text
        font = pygame.font.Font(None, 48)
        text = font.render("Jim Corbett National Park", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width//2, 50))
        # Add text background for better visibility
        bg_rect = text_rect.inflate(20, 10)
        bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(bg_surface, (0, 0, 0, 128), bg_surface.get_rect())
        screen.blit(bg_surface, bg_rect)
        screen.blit(text, text_rect)
        
        # Mountains in background
        mountain_color = (101, 67, 33)  # Brown
        mountain_points = [(0, self.height - 200)]
        for x in range(0, self.width + 100, 100):
            y = self.height - 200 + math.sin(x * 0.02) * 50
            mountain_points.append((x, y))
        mountain_points.append((self.width, self.height - 200))
        mountain_points.append((self.width, self.height))
        mountain_points.append((0, self.height))
        pygame.draw.polygon(screen, mountain_color, mountain_points)
        
        # Trees
        tree_positions = [(100, self.height - 150),
                         (300, self.height - 170),
                         (500, self.height - 160),
                         (700, self.height - 180)]
        
        for x, y in tree_positions:
            # Tree trunk
            trunk_color = (139, 69, 19)  # Brown
            pygame.draw.rect(screen, trunk_color,
                           (x - 10, y, 20, 80))
            
            # Tree canopy
            canopy_color = (34, 139, 34)  # Forest green
            pygame.draw.circle(screen, canopy_color,
                             (x, y - 20), 40)
            pygame.draw.circle(screen, canopy_color,
                             (x - 20, y - 10), 30)
            pygame.draw.circle(screen, canopy_color,
                             (x + 20, y - 10), 30)
        
        # Wedding stage platform
        stage_color = (255, 255, 255)  # White platform
        pygame.draw.rect(screen, stage_color,
                        (self.wedding_stage_x, self.wedding_stage_y, 150, 50))
        
        # Wedding arch
        arch_color = (255, 192, 203)  # Pink
        arch_rect = pygame.Rect(self.wedding_stage_x - 10,
                              self.wedding_stage_y - 80, 170, 100)
        pygame.draw.arc(screen, arch_color, arch_rect, 0, math.pi, 5)
        
        # Flowers on arch
        flower_colors = [(255, 0, 0),    # Red
                        (255, 192, 203),  # Pink
                        (255, 255, 0)]    # Yellow
        
        for i in range(10):
            x = self.wedding_stage_x + i * 17
            y = self.wedding_stage_y - 70 + math.sin(i * 0.5) * 10
            color = flower_colors[i % len(flower_colors)]
            pygame.draw.circle(screen, color, (x, y), 8)
        
        # Animate tigers
        for tiger in self.tiger_positions:
            x, y, direction = tiger
            
            # Update tiger position (walking animation)
            tiger[0] += direction * 1  # Move left or right
            
            # Reverse direction if tiger reaches screen bounds
            if tiger[0] < 200 or tiger[0] > self.width - 300:
                tiger[2] *= -1  # Reverse direction
            
            # Draw tiger
            tiger_color = (255, 140, 0)  # Orange
            # Tiger body
            pygame.draw.ellipse(screen, tiger_color,
                              (x - 30, y - 20, 60, 40))
            # Tiger head
            pygame.draw.circle(screen, tiger_color,
                             (x + (20 * direction), y - 10), 15)
            # Tiger stripes
            stripe_color = (0, 0, 0)  # Black
            for i in range(3):
                stripe_x = x - 15 + (i * 20)
                pygame.draw.line(screen, stripe_color,
                               (stripe_x, y - 30),
                               (stripe_x, y - 10), 3)
        
        # Draw heart when target is reached
        if not self.target_reached:
            heart_color = (255, 192, 203)  # Pink
            heart_x = self.wedding_stage_x + 80
            heart_y = self.wedding_stage_y - 20
            pygame.draw.circle(screen, heart_color,
                             (heart_x - 10, heart_y - 10), 15)
            pygame.draw.circle(screen, heart_color,
                             (heart_x + 10, heart_y - 10), 15)
            pygame.draw.polygon(screen, heart_color,
                              [(heart_x - 20, heart_y - 5),
                               (heart_x, heart_y + 20),
                               (heart_x + 20, heart_y - 5)])
    
    def check_target(self, player_x, player_y, boy_x, boy_y):
        # Check if both characters are on the wedding stage
        stage_rect = pygame.Rect(self.wedding_stage_x,
                               self.wedding_stage_y - 10,
                               150, 60)
        
        player_on_stage = stage_rect.collidepoint(player_x, player_y)
        boy_on_stage = stage_rect.collidepoint(boy_x, boy_y)
        
        if player_on_stage and boy_on_stage:
            self.target_reached = True
            return True
        return False
