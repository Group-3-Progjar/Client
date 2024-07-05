from game.scenes.scene import Scene
from game.objects.ui.board import Board
import pygame

class LeaderboardScene(Scene):
    def __init__(self, game: pygame):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)

        super().addEntity('board', Board(self, 100, 50, 600, 400))
        #self.game.entities['board'].textLeaderBoard.changeFont('assets/Pixeltype.ttf', 100)





