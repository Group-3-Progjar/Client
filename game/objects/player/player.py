from game.objects.gameobject import GameObject

class Player(GameObject):
    def __init__(self, scene, image, x, y, game):
        super().__init__(scene, image, x, y)
        
        self.score = 0
        self.isSliding = False
        self.game = game
        self.game.add_skin_id_observer(self.on_skin_id_change)

        #default x, y is (50, 320)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.delayDoubleJump = 100
        self.delayRun = 6
        self.initJumpSpeed = 16
        self.jumpCount = 0
        self.jumpSpeed = self.initJumpSpeed
        self.runIndex = 0

        self.pressed = False
        self.penguin_asset = ''
        self.on_skin_id_change(self.game.skin_id)


    def on_skin_id_change(self, skin_id):
        if skin_id == 1:
            self.penguin_asset = ''
        elif skin_id == 2:
            self.penguin_asset = '_2'


#work on logic
    def update(self):
        pgImage = self.scene.game.pygame.image
        if not self.scene.game.isOver():
            if self.isSliding:
                ground = 350
                self.scene.gravity *= 1.25
            else: 
                ground = 320
                self.scene.gravity = self.scene.initGravity

            if self.jumpCount > 0 and self.jumpCount <= 2:
                self.rect.y -= self.jumpSpeed
                self.jumpSpeed -= self.scene.gravity

            if self.rect.y < ground:
                self.rect.y += self.scene.gravity
                if self.rect.y > ground:
                    self.rect.y = ground
                    self.jumpCount = 0
                    self.jumpSpeed = self.initJumpSpeed
                
            if self.rect.y > ground:
                    self.rect.y = ground
                    self.jumpCount = 0
                    self.jumpSpeed = self.initJumpSpeed

            if self.jumpSpeed < 0 and not self.isSliding:
                    self.image = pgImage.load('assets/player_jump' + self.penguin_asset + '.png').convert_alpha()


            self.score += 0.1

            if self.delayDoubleJump != 0 and self.jumpCount == 2:
                self.delayDoubleJump -= 1
                if self.delayDoubleJump == 0:
                    self.image = pgImage.load('assets/player_jump' + self.penguin_asset + '.png').convert_alpha()
            
            if (not self.isSliding and self.jumpCount == 0) and not self.pressed:
                self.delayRun -= 1
                if self.delayRun == 0:
                    self.image = pgImage.load('assets/player_walk_' + str((self.runIndex % 4) + 1) + self.penguin_asset + '.png').convert_alpha()
                    self.runIndex += 1
                    self.delayRun = 6

    
    def handleEvents(self, events):
        pg = self.scene.game.pygame
        #keyboard controls
        for event in events:
            if self.scene.game.isPlay():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE or event.key == pg.K_UP:
                        if self.jumpCount < 2 and not self.isSliding:
                            self.jumpCount += 1
                            self.jumpSpeed = self.initJumpSpeed

                            if self.jumpCount == 2:
                                self.delayDoubleJump = 50
                                self.image = pg.image.load('assets/player_double_jump' + self.penguin_asset + '.png').convert_alpha()
                            else:
                                self.image = pg.image.load('assets/player_jump' + self.penguin_asset + '.png').convert_alpha()

                    elif event.key == pg.K_DOWN:
                        self.isSliding = True
                        self.image = pg.image.load('assets/player_slide' + self.penguin_asset + '.png').convert_alpha()
                        self.rect = self.image.get_rect(topleft=(50, 350 if self.jumpCount == 0 else self.rect.y))

                
                elif event.type == pg.KEYUP:
                    if self.isSliding:
                        self.image = pg.image.load('assets/player_walk_1' + self.penguin_asset + '.png').convert_alpha()
                        self.rect = self.image.get_rect(topleft=(50, 350 if self.jumpCount == 0 else self.rect.y))
                        self.isSliding = False

            elif self.scene.game.isMenu():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        self.pressed = True
                        self.image = pg.image.load('assets/player_over' + self.penguin_asset + '.png').convert_alpha()
                
                elif event.type == pg.MOUSEBUTTONUP:
                    self.pressed = False
    
    def render(self):
        self.scene.game.screen.blit(self.image, self.rect)


    def refresh(self):
        self.score = 0
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.isSliding = False
        self.delayDoubleJump = 100
        self.delayRun = 6
        self.jumpCount = 0
        self.jumpSpeed = 10
        self.runIndex = 0

            
        
            
