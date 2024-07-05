from game.objects.ui.text import GameText

class Board:
    def __init__(self, scene, x, y, width, height, font_size=24):
        self.scene = scene
        self.rect = self.scene.game.pygame.Rect(x, y, width, height)
        self.textLeaderBoard = GameText(scene, 'Leaderboard', 400, 75)
        self.placement = GameText(scene, '1st - Dummy', 250, 150)


    def update(self):
        pass

    def handleEvents(self, events):
        pass

    def render(self):
        self.scene.game.pygame.draw.rect(self.scene.game.screen, color="Blue", rect=self.rect)
        self.textLeaderBoard.render()
        self.placement.render()