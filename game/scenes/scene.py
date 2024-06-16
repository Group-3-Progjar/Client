import pygame
class Scene:
    def __init__(self, game:pygame, images:list):
        self.game = game
        #static images
        self.backgroundImages = []


        #sky, sun, etc

        # index 0 : image path
        # index 1 : location on screen (x, y) tuple
        for image in images:
            self.backgroundImages.append((self.game.pygame.image.load(image[0]), image[1]))

        self.initGravity = 1
        self.gravity = self.initGravity

    
    def addEntity(self,name, entity):
        self.game.entities[name] = entity

    def removeEntity(self,name):
        if name in self.game.entities:
            del self.game.entities[name]
        else:
            print(f"Entity '{name}' does not exist and cannot be removed.")

    def update(self):
        for name, entity in list(self.game.entities.items()):
            entity.update()

    def handleEvents(self, events):
        for name, entity in list(self.game.entities.items()):
            entity.handleEvents(events)

    def render(self):
        for image in self.backgroundImages:
            self.game.screen.blit(image[0], image[1])

        # order matters here
        for name, entity in list(self.game.entities.items()):
            entity.render()

    def reorderEntity(self, order):
        reordered = {key: self.game.entities[key] for key in order if key in self.game.entities}

        for name, entity in list(self.game.entities.items()):
            if name not in reordered:
                reordered[name] = entity
        
        self.game.entities = reordered
