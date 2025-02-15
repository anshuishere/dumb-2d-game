import pygame

class Hurdle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 60
        self.color = (0, 100, 0)  # Dark green

    def draw(self, screen):
        # Draw main hurdle body
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Draw some details
        detail_color = (0, 150, 0)  # Lighter green
        pygame.draw.rect(screen, detail_color, (self.x + 5, self.y + 10, self.width - 10, 5))
