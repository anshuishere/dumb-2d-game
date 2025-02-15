import pygame

class BoyCharacter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30  # Same as Shani's character
        self.height = 50  # Same as Shani's character
        self.speed = 5
        self.is_happy = False
        
    def draw(self, screen):
        # Body
        body_color = (70, 130, 180)  # Steel blue for shirt
        pygame.draw.rect(screen, body_color, 
                        (self.x, self.y, self.width, self.height))
        
        # Head
        face_color = (255, 218, 185)  # Peach
        pygame.draw.circle(screen, face_color,
                         (self.x + self.width//2, self.y - 5),
                         15)  # Smaller head
        
        # Simple hair (just a black semi-circle)
        hair_color = (0, 0, 0)  # Black
        pygame.draw.arc(screen, hair_color,
                       (self.x + 2, self.y - 20, 26, 30),
                       3.14, 6.28, 5)  # Top semicircle for hair
        
        # Simple eyes (just dots)
        if self.is_happy:
            # Happy eyes (small curved lines)
            pygame.draw.arc(screen, (0, 0, 0),
                          (self.x + 8, self.y - 8, 6, 6),
                          0, 3.14, 2)
            pygame.draw.arc(screen, (0, 0, 0),
                          (self.x + 18, self.y - 8, 6, 6),
                          0, 3.14, 2)
        else:
            # Normal eyes (simple dots)
            pygame.draw.circle(screen, (0, 0, 0),
                             (self.x + 10, self.y - 5), 2)
            pygame.draw.circle(screen, (0, 0, 0),
                             (self.x + 20, self.y - 5), 2)
    
    def check_collision(self, other):
        return (abs(self.x - other.x) < 40 and
                abs(self.y - other.y) < 40)
