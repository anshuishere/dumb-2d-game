import pygame
import math

class AllenBackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def draw(self, screen):
        # Sky gradient (desert sunset)
        for i in range(self.height):
            # Create a gradient from orange to light blue
            factor = i / self.height
            r = int(255 * (1 - factor * 0.5))  # Keep some orange
            g = int(200 * (1 - factor * 0.7))  # Fade orange to blue
            b = int(150 + factor * 105)        # Increase blue at top
            color = (r, g, b)
            pygame.draw.line(screen, color, (0, i), (self.width, i))
        
        # Desert sand dunes
        sand_color = (238, 198, 132)  # Desert sand
        dune_points = [(0, self.height)]
        for x in range(0, self.width + 100, 100):
            y = self.height - 100 + math.sin(x * 0.02) * 30
            dune_points.append((x, y))
        dune_points.append((self.width, self.height))
        pygame.draw.polygon(screen, sand_color, dune_points)
        
        # Darker sand details
        darker_sand = (205, 170, 109)
        for x in range(0, self.width, 50):
            y = self.height - 90 + math.sin(x * 0.02) * 20
            pygame.draw.line(screen, darker_sand, 
                           (x, y), (x + 30, y + 10), 3)
        
        # Allen Institute Building (modern architecture)
        building_color = (240, 230, 220)  # Light sandstone color
        building_x = self.width // 4
        building_y = self.height - 300
        
        # Main building structure
        pygame.draw.rect(screen, building_color,
                        (building_x, building_y, 300, 200))
        
        # Windows (modern pattern)
        window_color = (135, 206, 235)  # Sky blue
        for i in range(5):
            for j in range(4):
                pygame.draw.rect(screen, window_color,
                               (building_x + 20 + i * 60,
                                building_y + 20 + j * 45,
                                40, 30))
        
        # Building entrance
        entrance_color = (160, 150, 140)
        pygame.draw.rect(screen, entrance_color,
                        (building_x + 120, building_y + 120,
                         60, 80))
        
        # "ALLEN" text
        font = pygame.font.Font(None, 48)
        text = font.render("ALLEN", True, (0, 0, 0))
        text_rect = text.get_rect(center=(building_x + 150,
                                        building_y - 20))
        # Add text background for better visibility
        bg_rect = text_rect.inflate(20, 10)
        bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(bg_surface, (255, 255, 255, 180),
                        bg_surface.get_rect())
        screen.blit(bg_surface, bg_rect)
        screen.blit(text, text_rect)
        
        # Add "KOTA" text
        kota_text = font.render("KOTA, RAJASTHAN", True, (0, 0, 0))
        kota_rect = kota_text.get_rect(center=(self.width//2,
                                              self.height - 50))
        # Add text background
        kota_bg = kota_rect.inflate(20, 10)
        kota_surface = pygame.Surface(kota_bg.size, pygame.SRCALPHA)
        pygame.draw.rect(kota_surface, (255, 255, 255, 180),
                        kota_surface.get_rect())
        screen.blit(kota_surface, kota_bg)
        screen.blit(kota_text, kota_rect)
        
        # Add some desert vegetation (small cacti)
        cactus_color = (50, 120, 50)
        for x in [100, 600, 700]:
            # Cactus body
            pygame.draw.rect(screen, cactus_color,
                           (x, self.height - 150, 20, 40))
            # Cactus arms
            pygame.draw.rect(screen, cactus_color,
                           (x - 10, self.height - 130, 10, 15))
            pygame.draw.rect(screen, cactus_color,
                           (x + 20, self.height - 140, 10, 15))
        
        # Add sun
        sun_color = (255, 200, 50)
        pygame.draw.circle(screen, sun_color,
                          (self.width - 100, 100), 40)
        # Sun rays
        for angle in range(0, 360, 30):
            end_x = self.width - 100 + math.cos(math.radians(angle)) * 60
            end_y = 100 + math.sin(math.radians(angle)) * 60
            pygame.draw.line(screen, sun_color,
                           (self.width - 100, 100),
                           (end_x, end_y), 3)
