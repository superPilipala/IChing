import pygame
def MainWindow():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("赛博算卦")
    keep_going = True

    while keep_going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

    pygame.quit()