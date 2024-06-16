
class Button:
    def __init__(self, scene, image, x, y, onClickFunc, *args, **kwargs):
        self.scene = scene
        self.x = x
        self.y = y
        self.image = self.scene.game.pygame.image.load(image)
        self.rect = self.image.get_rect(midtop=(self.x, self.y))
        self.onClickFunc = onClickFunc
        self.pressed = False
        self.args = args
        self.kwargs = kwargs

    def update(self):
        self.rect = self.image.get_rect(midtop=(self.x, self.y))
        if self.rect.collidepoint(self.scene.game.pygame.mouse.get_pos()):
            self.rect = self.image.get_rect(midtop=(self.x, self.y-10))
                

    def handleEvents(self, events):
        pg = self.scene.game.pygame
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.pressed = True
            elif event.type == pg.MOUSEBUTTONUP:
                if self.pressed and self.rect.collidepoint(event.pos):
                    self.onClickFunc(*self.args, **self.kwargs)
                self.pressed = False



    def render(self):
        self.scene.game.screen.blit(self.image, self.rect)
    
    def reset(self):
        self.pressed = False
