from game.scenes.scene import Scene
from game.objects.obstacles.obstacle import Obstacles, Obstacle
from game.objects.ui.text import GameText

class PlayScene(Scene):
    def __init__(self, game):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)

        
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
        if 'score_text' in self.game.entities:
            self.game.entities['score_text'].changeText(f"Score :{str(int(player.score))}")

    def playerCollide(self, args):
        player = self.game.entities['player_you']
        player.image = self.game.pygame.image.load('assets/player_over.png').convert_alpha()
        player.isSliding = False
        player.jumpCount = 0
        super().removeEntity('score_text')
        self.game.changeScene('GAMEOVER')

