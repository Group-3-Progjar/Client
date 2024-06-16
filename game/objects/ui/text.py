from game.objects.gameobject import GameObject

class GameText:
    def __init__(self, scene, text, x, y, color='White'):
        self.scene = scene
        self.text = self.scene.game.scoreFont.render(text, False, color)
        self.rect = self.text.get_rect(midtop=(x,y))

    def update(self):
        pass

    def handleEvents(self, events):
        pass

    def render(self):
        self.scene.game.screen.blit(self.text, self.rect)
