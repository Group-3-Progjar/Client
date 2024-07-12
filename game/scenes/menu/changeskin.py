from game.scenes.scene import Scene
from game.objects.player.player import Player
from game.objects.background.clouds import Clouds
from game.objects.background.ground import Ground
from game.objects.ui.text import GameText
from game.objects.ui.button import Button

list_maps = {
    1: "Pinggo",
    2: "Pingbit",
    }

chosen_skin = 1

class ChangeSkinScene(Scene):
    def __init__(self, game, game_client):
        self.game_client = game_client
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)

        # the entity who gets added first will be rendered first
        super().addEntity('cr_clouds', Clouds(self))
        if self.game.skin_id == 1:
            super().addEntity('cr_player_you', Player(self, 'assets/player_walk_1.png', 50 , 320, game))
        else:
            super().addEntity('cr_player_you', Player(self, 'assets/player_walk_1_2.png', 50 , 320, game))
        super().addEntity('cr_ground', Ground(self,0))
        super().addEntity('cr_text_name', GameText(self, 'Choose Skin', 400, 100))
        super().addEntity('cr_map_1', Button(self, 'assets/skin1.png', 300, 175, self.chooseSkin, 1))
        # super().addEntity('cr_map_2', Button(self, 'assets/map_dirt.png', 400, 175, self.chooseMap, 2))
        super().addEntity('cr_map_3', Button(self, 'assets/skin2.png', 500, 175, self.chooseSkin, 2))
        super().addEntity('cr_text_players2', GameText(self, f'Skin: {list_maps[chosen_skin]}', 120, 10))
        super().addEntity('cr_start_button4', Button(self, 'assets/btn_confirm.png', 400, 360, self.game.changeScene, 'MENU'))
        
    def chooseSkin(self, skin_id):
        global chosen_skin
        chosen_skin = skin_id
        super().addEntity('cr_text_players2', GameText(self, f'Skin: {list_maps[chosen_skin]}', 120, 10))
        self.game.client.send_request("UPDATE_SKIN", {"username":self.game.username, "skin_id": chosen_skin})
        self.game.skin_id = chosen_skin
