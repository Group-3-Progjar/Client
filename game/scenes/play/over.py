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

        self.game.client.send_request('UPDATE_PROGRESS', {"leaderboard_id": self.game.leaderboard_id, "username": self.game.username, "score": self.game.entities['player_you'].score})

        # super().addEntity('over_text_restart', GameText(self, 'Click to Restart', 400, 250))
        super().addEntity('over_text_over', GameText(self, 'Game Over', 400, 150))
        super().addEntity('over_over_score', GameText(self, f"Score :{str(int(self.game.entities['player_you'].score))}", 400, 200))
        super().addEntity('over_start_button', Button(self, 'assets/btn_menu.png', 400, 280, self.goback))

    def goback(self):
        self.game.client.send_request("SEND_CHAT", {"username": self.game.username, "chat": f'Has Scored {round(self.game.entities["player_you"].score, 2)} Points'})
        self.game.changeScene('MENU')        