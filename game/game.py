from game.scenes.menu.menu import MenuScene
from game.scenes.play.play import PlayScene
from game.scenes.gameover.over import GameOverScene
from threading import Lock

class Game:
    def __init__(self, pygame, screen):
        self.lock = Lock()
        self.pygame = pygame
        self.screen = screen
        self.running = True

        self.clock = self.pygame.time.Clock()
        self.fps = 60

        self.scoreFont = self.pygame.font.Font('assets/Pixeltype.ttf', 50)
        self.gameFont = self.pygame.font.Font('assets/Pixeltype.ttf', 80)

        # moving objects
        self.entities = dict()

        self.scene = MenuScene(self)

    def run(self):
        while self.running:
            events = self.pygame.event.get()
            for event in events:
                if event.type == self.pygame.QUIT:
                    self.running = False
                    break  # Exit the event loop

            if not self.running:
                break  # Exit the game loop

            self.scene.handleEvents(events)
            self.scene.update()
            self.scene.render()
            self.pygame.display.flip()
            self.clock.tick(self.fps)

        self.pygame.quit()

    def changeScene(self, type):
        with self.lock:
            if type == 'STARTGAME':
                self.scene = PlayScene(self)
            if type == 'GAMEOVER':
                self.scene = GameOverScene(self)

    def isMenu(self):
        return isinstance(self.scene, MenuScene)

    def isPlay(self):
        return isinstance(self.scene, PlayScene)
    
    def isOver(self):
        return isinstance(self.scene, GameOverScene)
