import pygame
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()
snake_block=10
snake_speed=30

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/3, display_height/3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2

    x1_change = 0
    y1_change = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        
        if x1 > display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_over = True
        
        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        pygame.draw.rect(display, black, [x1, y1, snake_block, snake_block])

        message("You Lost", red)
        pygame.display.update()
        clock.tick(snake_speed)


pygame.quit()
quit()