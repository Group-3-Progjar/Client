
class GameObject:
    def __init__(self, scene, image, x, y):
        self.scene = scene
        self.image = self.scene.game.pygame.image.load(image)
        self.x = x
        self.y = y

    def update(self):
        pass

    def handleEvents(self, events):
        pass

    def render(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
            
        self.scene.game.screen.blit(self.image, (x, y))
