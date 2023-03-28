import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
    
    def broadcast(self, message, client):
        for c in self.clients:
            if c != client:
                c.send(message)
    
    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                if message:
                    self.broadcast(message, client)
                else:
                    self.remove(client)
            except:
                self.remove(client)
                break
    
    def remove(self, client):
        if client in self.clients:
            self.clients.remove(client)
    
    def run(self):
        while True:
            client, address = self.server_socket.accept()
            self.clients.append(client)
            print(f"{address[0]}:{address[1]} connected")
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()

if __name__ == '__main__':
    chat_server = ChatServer('localhost', 8888)
    chat_server.run()
