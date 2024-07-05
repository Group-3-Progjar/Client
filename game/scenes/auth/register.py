from game.objects.ui.text_input import TextInput
from game.scenes.scene import Scene
from game.objects.player.player import Player
from game.objects.background.clouds import Clouds
from game.objects.background.ground import Ground
from game.objects.ui.text import GameText
from game.objects.ui.button import Button

username=""
password=""
email=""

def unameCallback(text):
    global username
    username = text

def pwordCallback(text):
    global password
    password = text

def emailCallback(text):
    global email
    email = text

class RegisterScene(Scene):
    def __init__(self, game):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)


        #the entity who gets added first will be rendered first
        super().addEntity('register_clouds', Clouds(self))
        super().addEntity('register_player_you', Player(self, 'assets/player_walk_1.png', 50 , 320))
        super().addEntity('register_ground', Ground(self,0))
        super().addEntity('register_text_name', GameText(self, 'Penguin Runner', 400, 50))
        super().addEntity('register_text_desc', GameText(self, 'Register', 400, 100))
        super().addEntity('register_input_email', TextInput(self, 300, 150, 200, 40, on_text_changed=emailCallback,placeholder="Enter email"))
        super().addEntity('register_input_username', TextInput(self, 300, 210, 200, 40, on_text_changed=unameCallback,placeholder="Enter username"))
        super().addEntity('register_input_pass', TextInput(self, 300, 270, 200, 40, on_text_changed=pwordCallback,placeholder="Enter password"))
        super().addEntity('register_start_button3', Button(self, 'assets/btn_register.png', 400, 330, self.register))
        super().addEntity('register_start_button4', Button(self, 'assets/btn_login.png', 400, 400, self.game.changeScene, 'LOGIN'))

    def register(self):
        self.game.client.send_request("REGISTER", {"username":username, "password": password, "email": email})
        self.game.changeScene('OTP')