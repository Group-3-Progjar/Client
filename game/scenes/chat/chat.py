import pygame

class ChatScene:
    def __init__(self, game, game_client):
        self.game = game
        self.screen_width = 1200
        self.chat_box_width = 400
        self.chat_messages = []
        self.game_client = game_client
        self.input_box = pygame.Rect(self.screen_width - self.chat_box_width + 10, 460, self.chat_box_width - 20, 30)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.font = pygame.font.Font(None, 24)
        self.game_client.register_callback("RECEIVE_CHAT", self.receive_chat_callback)

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color_inactive
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        self.send_chat_message(self.text)
                        # self.chat_messages.append(('you', self.text))
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

    def send_chat_message(self, message):
        self.game_client.send_request("SEND_CHAT", {"username": self.game.username, "chat": message})

    def receive_chat_callback(self, data):
        print(f"Receive Chat22: {data}")
        self.chat_messages.append((data["username"], data["chat"]))

    def update(self):
        pass

    def render(self):
        # Draw chat background
        pygame.draw.rect(self.game.screen, (30, 30, 30), (800, 0, 400, 500))
        
        # Draw chat messages
        for i, (sender, message) in enumerate(self.chat_messages[-15:]):
            display_text = f"{sender}: {message}"
            txt_surface = self.font.render(display_text, True, (255, 255, 255))
            self.game.screen.blit(txt_surface, (810, 10 + i * 30))
        
        # Draw input box
        txt_surface = self.font.render(self.text, True, self.color)
        width = min(380, max(200, txt_surface.get_width() + 10))
        self.input_box.w = width
        self.game.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        pygame.draw.rect(self.game.screen, self.color, self.input_box, 2)
