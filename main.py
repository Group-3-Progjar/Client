import pygame
from game.game import Game

def main():
    print('heloo')
    pygame.init()
    screen = pygame.display.set_mode((1200, 500))
    pygame.display.set_caption('Penguin Runner')

    game = Game(pygame, screen)

    game.run()


if __name__=='__main__':
    main()