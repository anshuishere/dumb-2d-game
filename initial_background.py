import pygame

class InitialBackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 16)  # Smaller font size
        
    def draw_label(self, screen, text, x, y, color=(0, 0, 0)):
        # White background for better readability
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        padding = 2
        bg_rect = (text_rect.x - padding, text_rect.y - padding,
                  text_rect.width + 2*padding, text_rect.height + 2*padding)
        pygame.draw.rect(screen, (255, 255, 255), bg_rect)
        screen.blit(text_surface, text_rect)
        
    def draw(self, screen):
        # Sky gradient (evening sky color common in Lucknow)
        for y in range(self.height):
            progress = y / self.height
            color = (
                int(135 + (250-135) * progress),  # More orange at bottom
                int(206 + (150-206) * progress),
                int(235 + (100-235) * progress)
            )
            pygame.draw.line(screen, color, (0, y), (self.width, y))
            
        # Sun (setting sun)
        sun_color = (255, 200, 50)
        pygame.draw.circle(screen, sun_color, (650, 100), 40)
        
        # Clouds
        cloud_color = (255, 255, 255, 180)
        self.draw_cloud(screen, 100, 80, cloud_color)
        self.draw_cloud(screen, 400, 60, cloud_color)
        self.draw_cloud(screen, 700, 120, cloud_color)
        
        # Bara Imambara (main building)
        building_color = (230, 210, 180)  # Sandstone color
        imambara_width = 300
        imambara_height = 200
        imambara_x = 200
        imambara_y = self.height - 300
        
        # Main structure
        pygame.draw.rect(screen, building_color, 
                        (imambara_x, imambara_y, imambara_width, imambara_height))
        
        # Add label for Bada Imam Bada in the middle of the building
        self.draw_label(screen, "Bada Imam Bada", 
                       imambara_x + imambara_width//2, 
                       imambara_y + imambara_height//2)
        
        # Domes
        dome_color = (210, 190, 160)
        # Central dome
        self.draw_dome(screen, imambara_x + imambara_width//2, imambara_y, 60, dome_color)
        # Side domes
        self.draw_dome(screen, imambara_x + 50, imambara_y + 30, 30, dome_color)
        self.draw_dome(screen, imambara_x + imambara_width - 50, imambara_y + 30, 30, dome_color)
        
        # Rumi Darwaza
        gate_color = (200, 180, 150)
        gate_width = 120
        gate_height = 180
        gate_x = 50
        gate_y = self.height - 280
        
        # Main arch
        pygame.draw.rect(screen, gate_color, (gate_x, gate_y, gate_width, gate_height))
        self.draw_arch(screen, gate_x, gate_y, gate_width, 80, gate_color)
        
        # Decorative elements
        detail_color = (180, 160, 130)
        for x in range(gate_x + 10, gate_x + gate_width, 20):
            pygame.draw.rect(screen, detail_color, (x, gate_y + 20, 10, 140))
            
        # Other buildings in background
        for x in [500, 600, 700]:
            height = 150 + (x % 50)
            pygame.draw.rect(screen, (200, 190, 170), 
                           (x, self.height - height - 50, 60, height))
            # Windows
            for y in range(3):
                pygame.draw.rect(screen, (150, 150, 150),
                               (x + 20, self.height - height + 20 + y*40, 20, 30))
        
        # Ground (park/garden common in Lucknow)
        ground_color = (100, 150, 50)
        pygame.draw.rect(screen, ground_color, (0, self.height - 50, self.width, 50))
        
        # Trees (common in Lucknow gardens)
        tree_positions = [150, 350, 550, 750]
        for x in tree_positions:
            self.draw_tree(screen, x, self.height - 80)
            
    def draw_cloud(self, screen, x, y, color):
        for offset in [(0, 0), (20, 0), (40, 0), (10, -10), (30, -10)]:
            pygame.draw.circle(screen, color, (x + offset[0], y + offset[1]), 15)
            
    def draw_dome(self, screen, x, y, size, color):
        pygame.draw.ellipse(screen, color, 
                          (x - size//2, y - size//2, size, size))
        # Spire
        pygame.draw.rect(screen, color, (x - 2, y - size//2 - 15, 4, 15))
        
    def draw_arch(self, screen, x, y, width, height, color):
        pygame.draw.arc(screen, color, (x, y, width, height*2), 0, 3.14, 3)
        
    def draw_tree(self, screen, x, y):
        # Trunk
        trunk_color = (101, 67, 33)
        pygame.draw.rect(screen, trunk_color, (x - 5, y - 30, 10, 40))
        # Leaves
        leaf_color = (40, 100, 40)
        pygame.draw.circle(screen, leaf_color, (x, y - 40), 20)
        pygame.draw.circle(screen, leaf_color, (x - 15, y - 30), 15)
        pygame.draw.circle(screen, leaf_color, (x + 15, y - 30), 15)
