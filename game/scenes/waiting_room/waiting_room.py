from game.objects.ui.text_input import TextInput
from game.scenes.scene import Scene
from game.objects.player.player import Player
from game.objects.background.clouds import Clouds
from game.objects.background.ground import Ground
from game.objects.ui.text import GameText
from game.objects.ui.button import Button

code=""

def codeCallback(text):
    global code
    code = text


class OnlineRoomsScene(Scene):
    def __init__(self, game, game_client):
        self.game_client = game_client
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)

        #the entity who gets added first will be rendered first
        super().addEntity('otp_clouds', Clouds(self))
        super().addEntity('otp_player_you', Player(self, 'assets/player_walk_1.png', 50 , 320))
        super().addEntity('otp_ground', Ground(self,0))
        super().addEntity('otp_text_name', GameText(self, 'Waiting for Others', 400, 50))
        super().addEntity('otp_text_desc', GameText(self, '1/4 Joined', 400, 100))
        # super().addEntity('otp_input_email', TextInput(self, 300, 150, 200, 40, on_text_changed=codeCallback,placeholder="Room Code"))
        super().addEntity('otp_start_button3', Button(self, 'assets/btn_confirm.png', 400, 290, self.register))

    def register(self):
        self.game.client.send_request("JOIN_ROOM", {"username":self.game.username, "room_id": code})
