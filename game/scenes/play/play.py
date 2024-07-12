from game.objects.background.clouds import Clouds
from game.objects.background.ground import Ground
from game.objects.player.player import Player
from game.scenes.scene import Scene
from game.objects.obstacles.obstacle import Obstacles, Obstacle
from game.objects.ui.text import GameText

class PlayScene(Scene):
    def __init__(self, game, client):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)

        self.client = client
        self.client.register_callback("UPDATE_PROGRESS", self.updateScoreCallback)
        self.list_players = []
        
        #delete unused entities
        #there's an error : KeyError
        super().removeEntity('obstacles')
        super().removeEntity('text_start')
        super().removeEntity('text_restart')
        super().removeEntity('text_name')
        super().removeEntity('text_over')
        super().removeEntity('over_score')
        super().removeEntity('text_desc')
        super().removeEntity('start_button')
        super().addEntity('clouds', Clouds(self))
        if self.game.skin_id == 1:
            super().addEntity('player_you', Player(self, 'assets/player_walk_1.png', 50 , 320, game))
        else:
            super().addEntity('player_you', Player(self, 'assets/player_walk_1_2.png', 50 , 320, game))
        super().addEntity('ground', Ground(self,0))

        super().addEntity('p1', GameText(self, '', 600, 20))
        super().addEntity('p2', GameText(self, '', 600, 50))
        super().addEntity('p3', GameText(self, '', 600, 80))

        self.client.send_request('UPDATE_PROGRESS', {"leaderboard_id": self.game.leaderboard_id, "username": self.game.username, "score": self.game.entities['player_you'].score})

        # You can reorder the entities using reorderEntity()
        # example :
        # super().reorderEntity(['player_you', 'clouds', 'ground'])
        # this makes the clouds cover the player


        #add entities
        super().addEntity('obstacles', Obstacles([
            Obstacle(self, 'assets/obs_tall.png', 1300, 250),
            Obstacle(self, 'assets/small_obs.png', 800, 350),
            Obstacle(self, 'assets/obs_fly.png', 2500, 230)
        ]))
        super().addEntity('score_text', GameText(self, f"Score :{str(int(self.game.entities['player_you'].score))}", 80, 25))

        self.game.entities['player_you'].refresh()

        #obstacles

    def update(self):
        for name, entity in list(self.game.entities.items()):
            if name == 'obstacles':
                entity.checkCollision(self.game.entities['player_you'], self.playerCollide, [self])
            entity.update()
        player = self.game.entities['player_you']
        player.score += 0.1
        
        last = self.get_last_element(self.list_players)

        if last:
            if last['score'] < player.score:
                self.game.client.send_request('UPDATE_PROGRESS', {"leaderboard_id": self.game.leaderboard_id, "username": self.game.username, "score": player.score})

        if 'score_text' in self.game.entities:
            self.game.entities['score_text'].changeText(f"Score :{str(int(player.score))}")

    def get_last_element(self, lst):
        if lst:  # Check if the list is not empty
            return lst[-1]  # Return the last element
        return None  # Return None if the list is empty

    def playerCollide(self, args):
        player = self.game.entities['player_you']
        player.image = self.game.pygame.image.load('assets/player_over.png').convert_alpha()
        player.isSliding = False
        player.jumpCount = 0
        super().removeEntity('score_text')
        self.game.changeScene('GAMEOVER')


    def updateScoreCallback(self, payload):
        self.list_players = payload['players']
        for i in range(len(payload['players'])):
            print(payload['players'][i])
            self.game.entities['p'+str(i+1)].changeText(str(payload['players'][i]['place']) + '. ' + payload['players'][i]['username'] + ': ' + str(int(payload['players'][i]['score'])))
