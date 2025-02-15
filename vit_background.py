import pygame
import math

class VITBackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def draw(self, screen):
        # Sky (bright blue for South Indian sunny weather)
        screen.fill((135, 206, 250))
        
        # Sun
        pygame.draw.circle(screen, (255, 255, 0), (700, 80), 50)
        
        # Palm trees
        self.draw_palm_trees(screen)
        
        # VIT Building
        building_color = (255, 248, 220)  # Cornsilk
        building_width = 400
        building_height = 250
        building_x = (self.width - building_width) // 2
        building_y = self.height//2 - building_height + 50
        
        # Main building
        pygame.draw.rect(screen, building_color, 
                        (building_x, building_y, building_width, building_height))
        
        # Windows
        window_color = (173, 216, 230)  # Light blue
        for row in range(5):
            for col in range(8):
                pygame.draw.rect(screen, window_color,
                               (building_x + 30 + col * 45,
                                building_y + 40 + row * 45,
                                30, 30))
        
        # VIT Logo and name
        font = pygame.font.Font(None, 72)
        text_surface = font.render("VIT", True, (0, 51, 102))  # Dark blue
        text_rect = text_surface.get_rect(center=(building_x + building_width//2, building_y + 30))
        screen.blit(text_surface, text_rect)
        
        # Ground (lush green for South India)
        pygame.draw.rect(screen, (34, 139, 34), (0, self.height - 50, self.width, 50))
        
        # Grass details
        self.draw_grass(screen)
        
    def draw_palm_trees(self, screen):
        for x in [50, 150, 650, 750]:
            # Trunk
            pygame.draw.rect(screen, (139, 69, 19), (x, self.height - 150, 20, 100))
            
            # Leaves
            leaf_color = (0, 100, 0)
            for angle in [30, 45, 60, 75, 90, 105, 120, 135, 150]:
                start_pos = (x + 10, self.height - 150)
                end_x = x + 10 + 40 * math.cos(math.radians(angle))
                end_y = self.height - 150 - 40 * math.sin(math.radians(angle))
                pygame.draw.line(screen, leaf_color, start_pos, (int(end_x), int(end_y)), 5)
                
    def draw_grass(self, screen):
        grass_color = (50, 205, 50)
        for x in range(0, self.width, 10):
            height = 10 + (x % 10)
            pygame.draw.line(screen, grass_color, 
                           (x, self.height - 50),
                           (x, self.height - 50 - height), 2)
