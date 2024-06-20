from game.objects.gameobject import GameObject

class Cloud(GameObject):
    def __init__(self, scene, image, x, y, resetSrc, resetDst, moveRate):
        super().__init__(scene, image, x, y)

        self.resetSrc = resetSrc
        self.resetDst = resetDst
        self.moveRate = moveRate

    

    def update(self):
        #reset cloud position
        if int(self.x) == self.resetSrc:
            self.x = self.resetDst

        self.x -= self.moveRate



class Clouds:
    def __init__(self, scene):
        self.clouds = []

        cloud2 = Cloud(scene, 'assets/cloud_2.png', 390, 60, -410, 390, 0.1)
        self.clouds.append(cloud2)

        cloud1_1 = Cloud(scene, 'assets/cloud1_1.png', 100, 90, -700, 100, 0.3)
        self.clouds.append(cloud1_1)

        cloud2_1 = Cloud(scene, 'assets/cloud2_1.png', 550, 120, -250, 550, 0.29)
        self.clouds.append(cloud2_1)


    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def handleEvents(self, events):
        pass

    def render(self):
        for cloud in self.clouds:
            cloud.render()
            cloud.render(x=cloud.x+800)
