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
        if self.game.skin_id == 1:
            super().addEntity('player_you', Player(self, 'assets/player_walk_1.png', 50 , 320, game))
        else:
            super().addEntity('player_you', Player(self, 'assets/player_walk_1_2.png', 50 , 320, game))

        #the entity who gets added first will be rendered first
        super().addEntity('clouds', Clouds(self))
        super().addEntity('ground', Ground(self,0))
        super().addEntity('text_name', GameText(self, 'Penguin Runner', 400, 50))
        super().addEntity('text_desc', GameText(self, 'Group 3', 400, 100))
        super().addEntity('game_start_button', Button(self, 'assets/btn_startgame.png', 400, 150, self.game.changeScene, 'CREATE_ROOM'))
        super().addEntity('leaderboard_button', Button(self, 'assets/btn_leaderboard.png', 400, 220, self.game.changeScene, 'LEADERBOARD'))
        super().addEntity('change_skin_button', Button(self, 'assets/btn_change_skin.png', 400, 290, self.game.changeScene, 'CHANGE_SKIN'))
        super().addEntity('quit_button', Button(self, 'assets/btn_quit.png', 400, 360, self.game.quit, 'STARTGAME'))

        #create_room for map selection
