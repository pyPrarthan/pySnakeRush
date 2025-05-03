import pygame
from snake import Snake
from food import Food

import math

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLOCK_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.large_font = pygame.font.SysFont("Arial", 48, bold=True)
        self.start_screen()

    def start_screen(self):
        clock = pygame.time.Clock()
        alpha = 0
        fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        fade_surface.fill((0, 0, 0))

        for _ in range(30):
            self.screen.fill((0, 0, 0))
            fade_surface.set_alpha(255 - alpha)
            title = self.large_font.render("🐍 pySnakeRush", True, GREEN)
            self.screen.blit(title, (SCREEN_WIDTH // 2 - 160, 140))
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            alpha += 8
            clock.tick(30)

        self.blink_prompt("Press any key to start")

    def blink_prompt(self, text):
        blink = True
        blink_timer = 0
        waiting = True
        while waiting:
            self.screen.fill((0, 0, 0))
            title = self.large_font.render("🐍 pySnakeRush", True, GREEN)
            self.screen.blit(title, (SCREEN_WIDTH // 2 - 160, 120))

            if blink:
                prompt = self.font.render(text, True, WHITE)
                self.screen.blit(prompt, (SCREEN_WIDTH // 2 - 120, 200))

            blink_timer += 1
            if blink_timer % 30 == 0:
                blink = not blink

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

            pygame.display.flip()
            pygame.time.Clock().tick(15)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.snake.change_direction(event.key)

    def update(self):
        self.snake.move()
        if self.snake.check_collision_with_food(self.food.position):
            self.snake.grow()
            self.food.reposition()
            self.score += 1

        if self.snake.check_self_collision() or self.snake.check_wall_collision():
            self.game_over()

    def draw(self):
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def game_over(self):
        pulse = 0
        clock = pygame.time.Clock()

        while True:
            self.screen.fill((0, 0, 0))
            pulse_size = 48 + int(4 * abs(math.sin(pulse / 10)))
            game_over_font = pygame.font.SysFont("Arial", pulse_size, bold=True)
            over_text = game_over_font.render("Game Over", True, RED)
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            retry_text = self.font.render("Press any key to restart", True, WHITE)

            self.screen.blit(over_text, (SCREEN_WIDTH // 2 - 150, 100))
            self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 50, 180))
            self.screen.blit(retry_text, (SCREEN_WIDTH // 2 - 140, 220))

            pygame.display.flip()
            pulse += 1
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.reset_game()
                    return

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
