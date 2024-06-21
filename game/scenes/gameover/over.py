from game.scenes.scene import Scene
from game.objects.ui.text import GameText
from game.objects.ui.button import Button

class GameOverScene(Scene):
    def __init__(self, game):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)

        super().addEntity('text_restart', GameText(self, 'Click to Restart', 400, 250))
        super().addEntity('text_over', GameText(self, 'Game Over', 400, 50))
        super().addEntity('over_score', GameText(self, f"Score :{str(int(self.game.entities['player_you'].score))}", 400, 100))
        super().addEntity('start_button', Button(self, 'assets/play_btn.png', 400, 180, self.game.changeScene, 'STARTGAME'))

        