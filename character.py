import pygame

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.speed = 5  # Add movement speed
        self.dress_color = (255, 105, 180)  # Pink
        self.skin_color = (255, 218, 185)  # Light skin tone
        self.hair_color = (139, 69, 19)  # Brown
        self.is_happy = False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        # Draw dress (triangular shape)
        points = [
            (self.x + self.width//2, self.y),  # top
            (self.x, self.y + self.height),    # bottom left
            (self.x + self.width, self.y + self.height)  # bottom right
        ]
        pygame.draw.polygon(screen, self.dress_color, points)
        
        # Draw head
        head_radius = 10
        head_pos = (self.x + self.width//2, self.y + head_radius)
        pygame.draw.circle(screen, self.skin_color, head_pos, head_radius)
        
        # Draw eyes
        eye_color = (0, 0, 0)  # Black
        pygame.draw.circle(screen, eye_color, (head_pos[0] - 4, head_pos[1] - 2), 2)
        pygame.draw.circle(screen, eye_color, (head_pos[0] + 4, head_pos[1] - 2), 2)
        
        # Draw smile based on state
        if self.is_happy:
            # Bigger, happier smile
            smile_rect = (head_pos[0] - 6, head_pos[1], 12, 8)
            pygame.draw.arc(screen, eye_color, smile_rect, 0, 3.14, 2)
        else:
            # Shy, smaller smile
            smile_rect = (head_pos[0] - 4, head_pos[1] + 2, 8, 4)
            pygame.draw.arc(screen, eye_color, smile_rect, 0.2, 2.94, 1)
        
        # Draw pigtails
        # Left pigtail
        pygame.draw.circle(screen, self.hair_color, 
                         (head_pos[0] - 12, head_pos[1] - 5), 6)
        # Right pigtail
        pygame.draw.circle(screen, self.hair_color, 
                         (head_pos[0] + 12, head_pos[1] - 5), 6)
        
        # Draw hair on top
        hair_rect = pygame.Rect(head_pos[0] - 10, head_pos[1] - 12, 20, 12)
        pygame.draw.ellipse(screen, self.hair_color, hair_rect)
