import socket
import threading
import json

class GameClient:
    def __init__(self, host='localhost', port=12345):
        self.server_address = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock = threading.Lock()
        self.connected = False
        self.callbacks = {}

    def connect(self):
        self.socket.connect(self.server_address)
        self.connected = True
        threading.Thread(target=self.listen_for_messages, daemon=True).start()

    def send_request(self, command, payload):
        if not self.connected:
            raise Exception("Client is not connected to the server")
        message = f"{command};{json.dumps(payload)}"
        with self.lock:
            self.socket.sendall(message.encode('utf-8'))

    def listen_for_messages(self):
        while self.connected:
            try:
                data = self.socket.recv(1024).decode('utf-8')
                if not data:
                    continue
                command, json_data = data.split(';', 1)
                payload = json.loads(json_data)
                print(payload)
                if command in self.callbacks:
                    self.callbacks[command](payload)
            except Exception as e:
                print(f"Error: {e}")
                #self.connected = False

    def register_callback(self, command, callback):
        self.callbacks[command] = callback

    def close(self):
        self.connected = False
        self.socket.close()
