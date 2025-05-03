# main.py
import pygame
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("🐍 pySnakeRush")
    clock = pygame.time.Clock()

    game = Game(screen)

    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen with black
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(10)  # Control frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
