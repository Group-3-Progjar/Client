from game.objects.ui.button import Button
from game.scenes.scene import Scene
from game.objects.ui.board import Board
import pygame

class LeaderboardScene(Scene):
    def __init__(self, game: pygame, client):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)
        self.client = client
        self.list_players = []
        self.client.register_callback("LEADERBOARD", self.leaderboardCallback)
        self.client.send_request("LEADERBOARD", {})

        super().addEntity('btn_back', Button(self, 'assets/btn_back.png', 50, 20, self.goback))

        # super().addEntity('board', Board(self, 100, 50, 600, 400))
        #self.game.entities['board'].textLeaderBoard.changeFont('assets/Pixeltype.ttf', 100)


    def leaderboardCallback(self, data):
        # super().removeEntity('board')
        list_players = data["players"]
        super().addEntity('board', Board(self, 100, 20, 600, 460, list_items=list_players))


    def goback(self):
        self.client.unregister_callback("LEADERBOARD")
        self.game.changeScene('MENU')




