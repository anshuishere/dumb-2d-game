import pygame

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def draw(self, screen):
        # Sky gradient (evening sky)
        sky_gradient = [(135, 206, 235), (255, 190, 150)]  # Light blue to orange
        for i in range(self.height//2):
            color = [
                int(sky_gradient[0][j] + (sky_gradient[1][j] - sky_gradient[0][j]) * (i / (self.height//2)))
                for j in range(3)
            ]
            pygame.draw.line(screen, color, (0, i), (self.width, i))
            
        # Draw distant buildings (silhouette)
        building_color = (80, 80, 100)
        for x in range(0, self.width, 100):
            height = 150 + (x % 50)
            pygame.draw.rect(screen, building_color, (x, self.height//2 - height, 80, height))
            
        # Draw Allen building (main focus)
        allen_building_color = (200, 180, 160)  # Beige color
        allen_width = 300
        allen_height = 250
        allen_x = (self.width - allen_width) // 2
        allen_y = self.height//2 - allen_height + 50
        
        # Main building
        pygame.draw.rect(screen, allen_building_color, (allen_x, allen_y, allen_width, allen_height))
        
        # Windows
        window_color = (220, 220, 250)
        for row in range(5):
            for col in range(6):
                pygame.draw.rect(screen, window_color,
                               (allen_x + 30 + col * 45,
                                allen_y + 40 + row * 45,
                                30, 30))
                
        # Allen sign
        font = pygame.font.Font(None, 72)
        text_surface = font.render("ALLEN", True, (0, 0, 150))  # Dark blue text
        text_rect = text_surface.get_rect(center=(allen_x + allen_width//2, allen_y + 30))
        screen.blit(text_surface, text_rect)
        
        # Road
        road_color = (60, 60, 60)
        pygame.draw.rect(screen, road_color, (0, self.height - 50, self.width, 30))
        
        # Road markings
        marking_color = (255, 255, 255)
        for x in range(0, self.width, 80):
            pygame.draw.rect(screen, marking_color, (x, self.height - 35, 40, 5))
            
        # Small shops and structures
        shop_colors = [(210, 180, 140), (180, 200, 170), (200, 170, 180)]
        for x in range(0, self.width, 200):
            if x != (self.width - allen_width) // 2:  # Don't place shops where Allen building is
                color = shop_colors[x//200 % len(shop_colors)]
                pygame.draw.rect(screen, color, (x, self.height - 120, 150, 70))
                # Shop windows
                pygame.draw.rect(screen, (200, 200, 220), (x + 20, self.height - 100, 110, 30))
