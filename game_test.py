import pygame, sys

screen_width = 600
screen_height = 400
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption("Start Screen")

text_font = pygame.font.SysFont('Jokerman', 45)

def draw_text(text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))

def start_screen():
    waiting = True
    while waiting:
        screen.fill((0,0,0))
        draw_text("Press [Space] to Start", text_font, (255,255,255), 50, 150)
        pygame.display.flip()
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def game_over():

    text_font = pygame.font.SysFont('Jokerman', 38)

    waiting = True
    while waiting:
        draw_text("Game Over", text_font, (255,255,255), 150, 150)
        pygame.display.flip()
        draw_text("Press [SPACE] to Restart", text_font, (255,255,255), 20, 200)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
