from game.objects.gameobject import GameObject
import random
import itertools

class Obstacle(GameObject):
    def __init__(self, scene, image, x, y):
        super().__init__(scene, image, x, y)

        self.initX = x
        self.initY = y

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    #need to fix rect and x and y
    def update(self):
        if self.scene.game.isPlay():
            self.x -= 10
        self.rect.x = self.x
            

    def checkCollision(self, entity):
        return entity.rect.colliderect(self.rect)


class Obstacles:
    def __init__(self, obstacles):
        self.obstacles = obstacles


    def update(self):
        for obstacle in self.obstacles:
            if obstacle.scene.game.isPlay():
                obstacle.update()
                if obstacle.x < -250:
                    newX = obstacle.initX + random.randrange(-200, 1000, 100)
                    if newX < 800:
                        newX += 800
                    obstacle.x = newX

    def handleEvents(self, events):
        pass

    def render(self):
        for obstacle in self.obstacles:
            obstacle.render()


    def checkCollision(self, entity, trueFunc, tArgs):
        for obstacle in self.obstacles:
            if obstacle.checkCollision(entity):
                trueFunc(*tArgs)