from game.objects.gameobject import GameObject

class Obstacle(GameObject):
    def __init__(self, scene, image, x, y):
        super().__init__(scene, image, x, y)

        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def checkCollision(entity):
        return entity.rect.colliderect(self.rect)


class Obstacles:
    def __init__(self, obstacles):
        self.obstacles = []


    def update(self):
        for obstacle in self.obstacles:
            obstacle.update()

    def handleEvents(self, events):
        pass

    def render():
        for obstacle in self.obstacles:
            obstacle.render()

    def checkCollision(entity, trueFunc, tArgs, falseFunc, fArgs):
        for obstacle in self.obstacles:
            if obstacle.checkCollision(entity):
                trueFunc(*tArgs)
            else:
                falseFunc(*fArgs)