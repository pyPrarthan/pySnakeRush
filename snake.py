# snake.py

import pygame

GREEN = (0, 255, 0)
BLOCK_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (BLOCK_SIZE, 0)  # Initially moving right

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        self.body.pop()  # Remove tail

    def grow(self):
        self.body.append(self.body[-1])  # Duplicate last segment

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != (0, BLOCK_SIZE):
            self.direction = (0, -BLOCK_SIZE)
        elif key == pygame.K_DOWN and self.direction != (0, -BLOCK_SIZE):
            self.direction = (0, BLOCK_SIZE)
        elif key == pygame.K_LEFT and self.direction != (BLOCK_SIZE, 0):
            self.direction = (-BLOCK_SIZE, 0)
        elif key == pygame.K_RIGHT and self.direction != (-BLOCK_SIZE, 0):
            self.direction = (BLOCK_SIZE, 0)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    def check_collision_with_food(self, food_pos):
        return self.body[0] == food_pos

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

    def check_wall_collision(self):
        head_x, head_y = self.body[0]
        return (
            head_x < 0 or head_x >= SCREEN_WIDTH or
            head_y < 0 or head_y >= SCREEN_HEIGHT
        )
