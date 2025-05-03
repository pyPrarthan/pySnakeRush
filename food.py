# food.py

import pygame
import random

RED = (255, 0, 0)
BLOCK_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400

class Food:
    def __init__(self):
        self.position = self._random_position()

    def _random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return (x, y)

    def reposition(self):
        self.position = self._random_position()

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))
