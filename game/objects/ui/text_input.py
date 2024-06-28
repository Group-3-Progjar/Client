class TextInput:
    def __init__(self, scene, x, y, width, height, on_text_changed=None, font_size=24, max_length=None, placeholder=""):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = self.scene.game.pygame.Rect(x, y, width, height)
        
        self.font = self.scene.game.pygame.font.Font(None, font_size)
        self.text = ""
        self.max_length = max_length
        self.placeholder = placeholder
        
        self.active = False
        self.color_inactive = self.scene.game.pygame.Color('lightskyblue3')
        self.color_active = self.scene.game.pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text_color = self.scene.game.pygame.Color('black')
        self.placeholder_color = self.scene.game.pygame.Color('white')

        self.on_text_changed = on_text_changed

    def handleEvents(self, events):
        for event in events:
            if event.type == self.scene.game.pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color_inactive
            
            if event.type == self.scene.game.pygame.KEYDOWN:
                if self.active:
                    old_text = self.text
                    if event.key == self.scene.game.pygame.K_RETURN:
                        print(self.text)  # You can replace this with any action
                        self.text = ""
                    elif event.key == self.scene.game.pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        if self.max_length is None or len(self.text) < self.max_length:
                            self.text += event.unicode
                    
                    if self.text != old_text and self.on_text_changed:
                        self.on_text_changed(self.text)

    def update(self):
        width = max(self.width, self.font.size(self.text)[0] + 10)
        self.rect.w = width

    def render(self):
        # Draw the input box
        self.scene.game.pygame.draw.rect(self.scene.game.screen, self.color, self.rect, 2)
        
        # Render the text
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
        elif not self.active:
            text_surface = self.font.render(self.placeholder, True, self.placeholder_color)
        else:
            text_surface = self.font.render("", True, self.text_color)
        
        # Blit the text
        self.scene.game.screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text

    def set_text(self, text):
        old_text = self.text
        self.text = text
        if self.text != old_text and self.on_text_changed:
            self.on_text_changed(self.text)

    def reset(self):
        old_text = self.text
        self.text = ""
        self.active = False
        self.color = self.color_inactive
        if old_text and self.on_text_changed:
            self.on_text_changed(self.text)