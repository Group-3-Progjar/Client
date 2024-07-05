from game.objects.ui.text import GameText
from game.scenes.menu.create_room import CreateRoomScene
from game.scenes.auth.login import LoginScene
from game.scenes.menu.menu import MenuScene
from game.scenes.auth.otp import OtpScene
from game.scenes.play.play import PlayScene
from game.scenes.play.over import GameOverScene
from game.scenes.chat.chat import ChatScene
from game.scenes.auth.register import RegisterScene
from threading import Lock
from game.game_client import GameClient  # Assuming the client class is saved in client.py
from game.scenes.menu.leaderboard import LeaderboardScene


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
        self.chat_active = False
        self.entities = dict()
        self.username = "guest"
        self.leaderboardid = -1


        # Initialize and connect the client
        self.client = GameClient()
        self.client.connect()

        self.chat_scene = ChatScene(self, self.client)
        self.scene = LoginScene(self, self.client)

        # Register callbacks for server responses
        self.client.register_callback('RESPONSE', self.handle_general_response)
        self.client.register_callback('ROOM', self.handle_room)
        self.client.register_callback('CLOSED_ROOM', self.handle_closed_room)

    def run(self):
        while self.running:
            events = self.pygame.event.get()
            for event in events:
                if event.type == self.pygame.QUIT:
                    self.running = False
                    break

            if not self.running:
                break

            self.scene.handleEvents(events)
            self.scene.update()
            self.scene.render()

            self.chat_scene.handleEvents(events)
            self.chat_scene.update()
            self.chat_scene.render()

            self.pygame.display.flip()
            self.clock.tick(self.fps)

        self.pygame.quit()

    def changeScene(self, type):
        with self.lock:
            if type == 'GAMEOVER':
                self.scene = GameOverScene(self)
            else:
                self.scene.removeAllEntities()

            if type == 'MENU':
                self.scene = MenuScene(self)
            if type == 'STARTGAME':
                self.scene = PlayScene(self)
            if type == 'CREATE_ROOM':
                self.scene = CreateRoomScene(self, self.client)
            if type == 'LIST_ROOM':
                self.scene = ChatScene(self)
            if type == 'CHANGE_SKIN':
                self.scene = PlayScene(self)
            if type == 'REGISTER':
                self.scene = RegisterScene(self)
            if type == 'LOGIN':
                self.scene = LoginScene(self, self.client)
            if type == 'OTP':
                self.scene = OtpScene(self)
            if type == 'LEADERBOARD':
                self.scene = LeaderboardScene(self)

    def quit(self, args):
        self.running = False

    def isMenu(self):
        return isinstance(self.scene, MenuScene)

    def isPlay(self):
        return isinstance(self.scene, PlayScene)
    
    def isOver(self):
        return isinstance(self.scene, GameOverScene)

    def handle_general_response(self, payload):
        print(f"Command Response: {payload}")
        self.scene.addEntity('server_response', GameText(self.scene, payload["message"], 400, 450))
        if payload['leaderboard_id']:
            self.leaderboardid = payload['leaderboard_id']
            print(self.leaderboardid)

    def handle_receive_chat(self, payload):
        print(f"Receive Chat: {payload}")

    def handle_room(self, payload):
        print(f"Room: {payload}")

    def handle_closed_room(self, payload):
        print(f"Closed Room: {payload}")
