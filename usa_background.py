import pygame

class USABackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def draw(self, screen):
        # Sky gradient
        for i in range(self.height):
            color = (135 - i//10, 206 - i//10, 235 - i//10)
            pygame.draw.line(screen, color, (0, i), (self.width, i))
            
        # Ground
        ground_color = (34, 139, 34)  # Forest green
        pygame.draw.rect(screen, ground_color,
                        (0, self.height - 100, self.width, 100))
        
        # Draw USA Flag at the top center
        flag_width = 160
        flag_height = 100
        flag_x = self.width//2 - flag_width//2
        flag_y = 20
        
        # White background
        pygame.draw.rect(screen, (255, 255, 255),
                        (flag_x, flag_y, flag_width, flag_height))
        
        # Red stripes
        stripe_height = flag_height // 13
        for i in range(0, 13, 2):
            pygame.draw.rect(screen, (178, 34, 34),  # Red
                           (flag_x, flag_y + i * stripe_height,
                            flag_width, stripe_height))
        
        # Blue canton
        canton_width = flag_width * 0.4
        canton_height = flag_height * 0.54
        pygame.draw.rect(screen, (0, 40, 104),  # Dark blue
                        (flag_x, flag_y, canton_width, canton_height))
        
        # Stars (simplified)
        star_rows = 9
        star_cols = 11
        star_spacing_x = canton_width / (star_cols + 1)
        star_spacing_y = canton_height / (star_rows + 1)
        for row in range(1, star_rows + 1):
            for col in range(1, star_cols + 1):
                star_x = flag_x + col * star_spacing_x
                star_y = flag_y + row * star_spacing_y
                pygame.draw.circle(screen, (255, 255, 255),
                                 (int(star_x), int(star_y)), 2)
        
        # Chicago Skyline (Left side)
        # Simplified Willis Tower
        pygame.draw.rect(screen, (40, 40, 60),  # Dark silhouette
                        (100, self.height - 400, 100, 300))
        # Top antennas
        pygame.draw.rect(screen, (40, 40, 60),
                        (130, self.height - 440, 15, 40))
        pygame.draw.rect(screen, (40, 40, 60),
                        (160, self.height - 430, 15, 30))
        
        # "CHICAGO" text
        font = pygame.font.Font(None, 48)
        text = font.render("CHICAGO", True, (255, 255, 255))
        text_rect = text.get_rect(center=(200, self.height - 50))
        # Add text background for better visibility
        bg_rect = text_rect.inflate(20, 10)
        pygame.draw.rect(screen, (0, 0, 0, 128), bg_rect)
        screen.blit(text, text_rect)
        
        # Bay Area (Right side)
        # Simplified Golden Gate Bridge
        bridge_color = (178, 34, 34)  # Firebrick red
        # Main span
        pygame.draw.rect(screen, bridge_color,
                        (self.width - 300, self.height - 250, 200, 10))
        # Left tower
        pygame.draw.rect(screen, bridge_color,
                        (self.width - 280, self.height - 350, 20, 200))
        # Right tower
        pygame.draw.rect(screen, bridge_color,
                        (self.width - 140, self.height - 350, 20, 200))
        
        # "BAY AREA" text
        text = font.render("BAY AREA", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width - 200, self.height - 50))
        # Add text background for better visibility
        bg_rect = text_rect.inflate(20, 10)
        pygame.draw.rect(screen, (0, 0, 0, 128), bg_rect)
        screen.blit(text, text_rect)
