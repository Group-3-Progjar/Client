from game.scenes.scene import Scene
from game.objects.player.player import Player
from game.objects.background.clouds import Clouds
from game.objects.background.ground import Ground
from game.objects.ui.text import GameText
from game.objects.ui.button import Button

list_maps = {
    1: "Ice Map",
    2: "Dirt Map",
    3: "Green Map"
    }

chosen_map = 1
players = 2

class CreateRoomScene(Scene):
    def __init__(self, game, game_client):
        self.game_client = game_client
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)
        self.game_client.register_callback("CREATE_ROOM", self.createRoomCallback)

        #the entity who gets added first will be rendered first
        super().addEntity('cr_clouds', Clouds(self))
        super().addEntity('cr_player_you', Player(self, 'assets/player_walk_1.png', 50 , 320))
        super().addEntity('cr_ground', Ground(self,0))
        super().addEntity('cr_text_name', GameText(self, 'Choose Map', 400, 50))
        super().addEntity('cr_map_1', Button(self, 'assets/map_ice.png', 180, 100, self.chooseMap, 1))
        super().addEntity('cr_map_2', Button(self, 'assets/map_dirt.png', 400, 100, self.chooseMap, 2))
        super().addEntity('cr_map_3', Button(self, 'assets/map_green.png', 620, 100, self.chooseMap, 3))
        super().addEntity('cr_text_players2', GameText(self, f'Map: {list_maps[chosen_map]}', 120, 10))
        super().addEntity('cr_p2', Button(self, 'assets/btn_2p.png', 180, 280, self.choosePlayers, 2))
        super().addEntity('cr_p3', Button(self, 'assets/btn_3p.png', 400, 280, self.choosePlayers, 3))
        super().addEntity('cr_p4', Button(self, 'assets/btn_4p.png', 620, 280, self.choosePlayers, 4))
        super().addEntity('cr_start_button4', Button(self, 'assets/btn_confirm.png', 400, 360, self.createRoom))
        
    def chooseMap(self, map_id):
        global chosen_map
        chosen_map = map_id
        super().addEntity('cr_text_players2', GameText(self, f'Map: {list_maps[chosen_map]}', 120, 10))

    def choosePlayers(self, player):
        global players
        players = player
        super().addEntity('cr_text_players3', GameText(self, f'Players: {players}', 90, 50))

    def createRoom(self):
        self.game.client.send_request("CREATE_ROOM", {"username":self.game.username, "map_id": chosen_map, "max_players": players})

    def createRoomCallback(self, data):
        if data["success"]:
            self.game.waitingRoom(data["room_id"])