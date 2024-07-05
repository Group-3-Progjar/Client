from game.objects.gameobject import GameObject

class GameText:
    def __init__(self, scene, text, x, y, color='White'):
        self.scene = scene
        self.textstring = text
        self.text = self.scene.game.scoreFont.render(text, False, color)
        self.rect = self.text.get_rect(midtop=(x,y))
        self.color = color


    def update(self):
        pass

    def handleEvents(self, events):
        pass

    def render(self):
        self.scene.game.screen.blit(self.text, self.rect)

    def changeText(self, text):
        self.text = self.scene.game.scoreFont.render(text, False, self.color)
    
    def changeFont(self, filePath, size):
        font = self.scene.game.pygame.font.Font(filePath, size)
        self.text = font.render(self.textstring, False, self.color)
