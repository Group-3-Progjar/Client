from game.objects.ui.text_input import TextInput
from game.scenes.scene import Scene
from game.objects.player.player import Player
from game.objects.background.clouds import Clouds
from game.objects.background.ground import Ground
from game.objects.ui.text import GameText
from game.objects.ui.button import Button

username=""
password=""

def unameCallback(text):
    global username
    username = text

def pwordCallback(text):
    global password
    password = text


class LoginScene(Scene):
    def __init__(self, game, game_client):
        self.game_client = game_client
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)
        self.game_client.register_callback("LOGIN", self.loginCallback)

        #the entity who gets added first will be rendered first
        super().addEntity('clouds', Clouds(self))
        super().addEntity('player_you', Player(self, 'assets/player_walk_1.png', 50 , 320))
        super().addEntity('ground', Ground(self,0))
        super().addEntity('text_name', GameText(self, 'Penguin Runner', 400, 50))
        super().addEntity('text_desc', GameText(self, 'Login', 400, 100))
        super().addEntity('input_email', TextInput(self, 300, 150, 200, 40, on_text_changed=unameCallback,placeholder="Enter username"))
        super().addEntity('input_pass', TextInput(self, 300, 210, 200, 40, on_text_changed=pwordCallback,placeholder="Enter password"))
        super().addEntity('start_button3', Button(self, 'assets/btn_login.png', 400, 290, self.login))
        super().addEntity('start_button4', Button(self, 'assets/btn_register.png', 400, 360, self.game.changeScene, 'REGISTER'))

    def login(self):
        self.game.client.send_request("LOGIN", {"username":username, "password": password})

    def loginCallback(self, data):
        if data["success"]:
            self.game.username = username
            self.game.changeScene('MENU')