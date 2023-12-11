import sys
import pygame
from pygame.locals import *
import startgame

img_basic_address = './img/'

class UNOGame():
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load(img_basic_address+'background.png')
        self.screen_width = 760
        self.screen_height = 550
        self.background_Color = (0,66,0)
        self.playernum = 2
        self.difficulty = 1
        self.font = 'Berlin Sans FB'
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(self.background_Color)
        self.screen.blit(self.background, (-30, -30))
        pygame.display.update()

    def text_format(self, message, textFont, textSize, textColor):
        newFont = pygame.font.SysFont(textFont, textSize)
        newText = newFont.render(message, K_0, textColor)
        return newText


    def main_menu(self):
        menu = True
        selected = 1
        while menu:
            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.init()
            sound = pygame.mixer.Sound('./sound/menu.wav')
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        sound.play()
                        if selected <=1:
                            selected = 1
                        else:
                            selected = selected-1
                    elif event.key == K_DOWN:
                        sound.play()
                        if selected >=3:
                            selected = 3
                        else:
                            selected = selected+1
                    if event.key == K_RETURN:
                        if selected <= 1:
                            self.background = pygame.image.load('./img/background.png')
                            self.screen.blit(self.background, (-30, -30))
                            game = startgame.game(self.playernum, self.difficulty)
                            game.startgame()
                        if selected >= 2:
                            pygame.quit()
                            sys.exit()
           
            if selected == 1:
                text_start = self.text_format("START", self.font, 50, (255,255,255))
            else:
                text_start = self.text_format("START", self.font, 50, (0,0,0))
            if selected == 2:
                text_quit = self.text_format("QUIT", self.font, 50, (255,255,255))
            else:
                text_quit = self.text_format("QUIT", self.font, 50, (0,0,0))

            start_rect = text_start.get_rect()
            quit_rect=text_quit.get_rect()

            self.screen.blit(text_start, (self.screen_width/2 - (start_rect[2]/2), 200))
            self.screen.blit(text_quit, (self.screen_width/2 - (quit_rect[2]/2), 260))
            pygame.display.update()
            self.clock.tick(self.FPS)
            pygame.display.set_caption("UNO!")

if __name__ == '__main__':
    uno = UNOGame()
    uno.main_menu()