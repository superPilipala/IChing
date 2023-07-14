import sys

import pygame

from IChing.IChing import IChing


class MainApp:
    BG = (0, 0, 0)
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    FPS = 30

    lao_yin_img = pygame.image.load('IChingGUi/images/老阴.png')
    lao_yang_img = pygame.image.load('IChingGui/images/老阳.png')
    yin_img = pygame.image.load('IChingGui/images/少阴.png')
    yang_img = pygame.image.load('IChingGui/images/少阳.png')

    def run(self):
        # 初始化
        pygame.init()
        window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        clock = pygame.time.Clock()

        pygame.display.set_caption("赛博算卦")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ic = IChing()
                    origin_div_array = ic.get_origin_div()
                    for div_symbol in origin_div_array:
                        if div_symbol.yin_yang:
                            if div_symbol.is_change:
                                window.blit(self.lao_yin_img, (100, 200))
                            else:
                                window.blit(self.yin_img, (100, 250))
            # window.blit(self.lao_yin_img, (100, 200))
            # window.fill(self.BG)

            pygame.display.update()

            clock.tick(self.FPS)

