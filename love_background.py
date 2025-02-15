import pygame

class LoveBackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.is_colorful = False
        self.transition_start = 0
        self.transition_duration = 1000  # 1 second for color transition
        self.met_boy = False
        
    def draw(self, screen, current_time):
        # Calculate transition factor (0 to 1) if transition is happening
        transition_factor = 0
        if self.met_boy:
            transition_factor = min(1.0, (current_time - self.transition_start) / self.transition_duration)
        
        # Background color (transitions from gray to light blue)
        if self.met_boy:
            gray = 200
            color_r = 135
            color_g = 206
            color_b = 235
            
            r = int(gray * (1 - transition_factor) + color_r * transition_factor)
            g = int(gray * (1 - transition_factor) + color_g * transition_factor)
            b = int(gray * (1 - transition_factor) + color_b * transition_factor)
        else:
            r = g = b = 200
        
        screen.fill((r, g, b))
        
        # Draw buildings
        building_positions = [
            (50, 200, 100, 300),  # (x, y, width, height)
            (200, 150, 120, 350),
            (370, 180, 90, 320),
            (510, 160, 110, 340),
            (670, 190, 80, 310)
        ]
        
        for x, y, width, height in building_positions:
            # Building base color (transitions from gray to beige)
            if self.met_boy:
                gray = 150
                building_r = 245
                building_g = 222
                building_b = 179
                
                r = int(gray * (1 - transition_factor) + building_r * transition_factor)
                g = int(gray * (1 - transition_factor) + building_g * transition_factor)
                b = int(gray * (1 - transition_factor) + building_b * transition_factor)
            else:
                r = g = b = 150
            
            # Main building
            pygame.draw.rect(screen, (r, g, b), (x, y, width, height))
            
            # Windows
            window_rows = height // 50
            window_cols = width // 30
            
            for row in range(window_rows):
                for col in range(window_cols):
                    # Window color (transitions from dark gray to yellow)
                    if self.met_boy:
                        gray = 100
                        window_r = 255
                        window_g = 255
                        window_b = 150
                        
                        wr = int(gray * (1 - transition_factor) + window_r * transition_factor)
                        wg = int(gray * (1 - transition_factor) + window_g * transition_factor)
                        wb = int(gray * (1 - transition_factor) + window_b * transition_factor)
                    else:
                        wr = wg = wb = 100
                    
                    window_x = x + 10 + col * 30
                    window_y = y + 20 + row * 50
                    
                    if window_x + 15 < x + width - 5:  # Ensure window is within building
                        pygame.draw.rect(screen, (wr, wg, wb),
                                       (window_x, window_y, 15, 20))
        
        # Ground
        if self.met_boy:
            gray = 150
            ground_r = 169
            ground_g = 169
            ground_b = 169
            
            r = int(gray * (1 - transition_factor) + ground_r * transition_factor)
            g = int(gray * (1 - transition_factor) + ground_g * transition_factor)
            b = int(gray * (1 - transition_factor) + ground_b * transition_factor)
        else:
            r = g = b = 150
            
        pygame.draw.rect(screen, (r, g, b),
                        (0, self.height - 100, self.width, 100))
        
        # Path with flowers
        if self.met_boy:
            gray = 180
            path_r = 200
            path_g = 200
            path_b = 200
            
            r = int(gray * (1 - transition_factor) + path_r * transition_factor)
            g = int(gray * (1 - transition_factor) + path_g * transition_factor)
            b = int(gray * (1 - transition_factor) + path_b * transition_factor)
        else:
            r = g = b = 180
            
        pygame.draw.rect(screen, (r, g, b),
                        (0, self.height - 50, self.width, 20))
        
        # Add flowers on the path that appear during transition
        if self.met_boy:
            flower_colors = [(255, 192, 203),  # Pink
                           (255, 255, 0),      # Yellow
                           (255, 0, 0),        # Red
                           (255, 165, 0)]      # Orange
            
            for x in range(0, self.width, 30):
                color_idx = (x // 30) % len(flower_colors)
                base_color = flower_colors[color_idx]
                
                # Transition from gray to colorful flowers
                r = int(180 * (1 - transition_factor) + base_color[0] * transition_factor)
                g = int(180 * (1 - transition_factor) + base_color[1] * transition_factor)
                b = int(180 * (1 - transition_factor) + base_color[2] * transition_factor)
                
                pygame.draw.circle(screen, (r, g, b),
                                 (x, self.height - 40), 5)
    
    def start_transition(self, current_time):
        self.met_boy = True
        self.transition_start = current_time
