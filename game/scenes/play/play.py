from game.scenes.scene import Scene

class PlayScene(Scene):
    def __init__(self, game):
        images = [
            ['assets/sky.png', (0,0)],
            ['assets/sun.png', (600, 20)]
        ]
        super().__init__(game, images)

        
        #delete unused entities
        #there's an error : KeyError
        super().removeEntity('text_start')
        super().removeEntity('text_name')
        super().removeEntity('text_desc')
        super().removeEntity('start_button')


        # You can reorder the entities using reorderEntity()
        # example :
        # super().reorderEntity(['player_you', 'clouds', 'ground'])
        # this makes the clouds cover the player


        #add entities

        #obstacles
