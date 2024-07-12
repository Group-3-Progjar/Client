from game.objects.ui.text import GameText

class Board:
    def __init__(self, scene, x, y, width, height, font_size=24, list_items=[]):
        self.scene = scene
        self.rect = self.scene.game.pygame.Rect(x, y, width, height)
        self.textLeaderBoard = GameText(scene, 'Leaderboard', 400, 30)
        self.list_text = []
        for i in range(len(list_items)):
            score = round(float(list_items[i]["score"]), 2)
            self.list_text.append(GameText(scene, f'{list_items[i]["place"]}. {list_items[i]["username"]}: {score}', 400, 70 + (i * 40)))
        # self.placement = GameText(scene, '1st - Dummy', 250, 150)


    def update(self):
        pass

    def handleEvents(self, events):
        pass

    def render(self):
        self.scene.game.pygame.draw.rect(self.scene.game.screen, color="Blue", rect=self.rect)
        self.textLeaderBoard.render()
        for i in range(len(self.list_text)):
            self.list_text[i].render()