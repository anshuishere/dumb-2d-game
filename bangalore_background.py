import pygame
import random

class BangaloreBackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 48)
        # Pre-generate building layout
        self.buildings = []
        building_colors = [(50, 50, 50), (60, 60, 60), (70, 70, 70)]
        for x in range(0, self.width, 100):
            self.buildings.append({
                'x': x,
                'height': random.randint(200, 300),
                'color': random.choice(building_colors)
            })
        
    def draw(self, screen):
        # Modern city sky (tech hub feel)
        screen.fill((135, 206, 235))  # Sky blue
        
        # Sun
        pygame.draw.circle(screen, (255, 255, 0), (100, 100), 40)
        
        # Modern buildings in background
        for building in self.buildings:
            x = building['x']
            height = building['height']
            color = building['color']
            # Main building
            pygame.draw.rect(screen, color, 
                           (x, self.height - height - 50, 80, height))
            # Windows
            for y in range(height // 40):
                for wx in range(2):
                    pygame.draw.rect(screen, (200, 200, 100), 
                                   (x + 15 + wx*30, 
                                    self.height - height - 30 + y*40, 20, 30))
        
        # Visa building (central, modern glass building)
        visa_building_x = self.width // 2 - 150
        visa_building_y = self.height - 400
        visa_building_width = 300
        visa_building_height = 350
        
        # Main building structure (glass-like blue)
        pygame.draw.rect(screen, (100, 149, 237), 
                        (visa_building_x, visa_building_y, 
                         visa_building_width, visa_building_height))
        
        # Glass window effect
        for y in range(visa_building_y, visa_building_y + visa_building_height, 30):
            for x in range(visa_building_x, visa_building_x + visa_building_width, 40):
                pygame.draw.rect(screen, (173, 216, 230), 
                               (x, y, 35, 25))
        
        # Visa logo
        logo_text = self.font.render("VISA", True, (255, 255, 255))
        logo_rect = logo_text.get_rect(center=(visa_building_x + visa_building_width//2,
                                              visa_building_y + 50))
        # Logo background
        pygame.draw.rect(screen, (0, 56, 168), 
                        (logo_rect.x - 10, logo_rect.y - 10,
                         logo_rect.width + 20, logo_rect.height + 20))
        screen.blit(logo_text, logo_rect)
        
        # Ground (modern pavement)
        pygame.draw.rect(screen, (120, 120, 120), (0, self.height - 50, self.width, 50))
        
        # Road markings
        for x in range(0, self.width, 100):
            pygame.draw.rect(screen, (255, 255, 255), (x, self.height - 30, 50, 5))
            
        # Trees (modern landscaping)
        tree_positions = [50, 200, 600, 750]
        for x in tree_positions:
            self.draw_modern_tree(screen, x, self.height - 80)
    
    def draw_modern_tree(self, screen, x, y):
        # Modern geometric tree design
        trunk_color = (90, 60, 30)
        leaf_color = (34, 139, 34)
        
        # Trunk
        pygame.draw.rect(screen, trunk_color, (x - 5, y - 30, 10, 40))
        
        # Angular foliage
        points = [(x, y - 70),
                 (x - 20, y - 30),
                 (x + 20, y - 30)]
        pygame.draw.polygon(screen, leaf_color, points)
        points = [(x, y - 90),
                 (x - 15, y - 60),
                 (x + 15, y - 60)]
        pygame.draw.polygon(screen, leaf_color, points)
