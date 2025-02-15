import pygame

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.color = (255, 215, 0)  # Gold
        
    def draw(self, screen):
        # Draw outer circle
        pygame.draw.circle(screen, self.color, (self.x + self.width//2, self.y + self.height//2), 15)
        # Draw inner circle
        pygame.draw.circle(screen, (255, 165, 0), (self.x + self.width//2, self.y + self.height//2), 8)
            
    def check_collision(self, character):
        char_rect = pygame.Rect(character.x, character.y, character.width, character.height)
        target_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return char_rect.colliderect(target_rect)
