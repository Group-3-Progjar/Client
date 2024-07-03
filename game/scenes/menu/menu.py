from game.scenes.scene import Scene
from game.objects.player.player import Player
from game.objects.background.clouds import Clouds
from game.objects.background.ground import Ground
from game.objects.ui.text import GameText
from game.objects.ui.button import Button


class MenuScene(Scene):
    def __init__(self, game):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)


        #the entity who gets added first will be rendered first
        super().addEntity('clouds', Clouds(self))
        super().addEntity('player_you', Player(self, 'assets/player_walk_1.png', 50 , 320))
        super().addEntity('ground', Ground(self,0))
        super().addEntity('text_name', GameText(self, 'Penguin Runner', 400, 50))
        super().addEntity('text_desc', GameText(self, 'Group 3', 400, 100))
        super().addEntity('start_button3', Button(self, 'assets/btn_startgame.png', 400, 150, self.game.changeScene, 'CREATE_ROOM'))
        super().addEntity('start_button2', Button(self, 'assets/btn_leaderboard.png', 400, 220, self.game.changeScene, 'STARTGAME'))
        super().addEntity('start_button4', Button(self, 'assets/btn_quit.png', 400, 360, self.game.quit, 'STARTGAME'))

        #create_room for map selection
