import pygame
import math

class LeafAnimation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active = False
        self.x = width // 2
        self.y = -50
        self.time = 0
        self.oscillation_speed = 0.05
        self.fall_speed = 2
        self.size = 40  # Increased size for better visibility
        self.rotation = 0
        self.rotation_speed = 2
        self.font = pygame.font.Font(None, self.size)
        
    def start(self):
        self.active = True
        self.x = self.width // 2
        self.y = -50
        self.time = 0
        self.rotation = 0
            
    def update(self):
        if not self.active:
            return
            
        self.time += self.oscillation_speed
        self.x = self.x + math.sin(self.time) * 3  # Gentle side-to-side movement
        self.y += self.fall_speed
        self.rotation += self.rotation_speed
        
        # Stop animation when emoji reaches bottom
        if self.y > self.height:
            self.active = False
            
    def draw(self, screen):
        if not self.active:
            return
            
        # Create a surface for the text with alpha channel
        text_surface = pygame.Surface((self.size * 2, self.size), pygame.SRCALPHA)
        
        # Render "420" with a green color
        text = self.font.render("420", True, (34, 139, 34))
        text_rect = text.get_rect(center=(self.size, self.size // 2))
        text_surface.blit(text, text_rect)
        
        # Rotate the text
        rotated_text = pygame.transform.rotate(text_surface, self.rotation)
        
        # Get the rect for positioning
        text_rect = rotated_text.get_rect(center=(int(self.x), int(self.y)))
        
        # Draw the rotated text
        screen.blit(rotated_text, text_rect)
