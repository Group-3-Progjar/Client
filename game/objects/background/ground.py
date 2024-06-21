from game.objects.gameobject import GameObject

class Ground(GameObject):
    def __init__(self, scene, x):
        super().__init__(scene,  'assets/ground.png', x, 400)


    def update(self):
        if not self.scene.game.isOver():
            if self.x <= -800:
                self.x = 0

            self.x -= 10

    def render(self):
        self.scene.game.screen.blit(self.image, (self.x, self.y))
        self.scene.game.screen.blit(self.image, (self.x+800, self.y))
