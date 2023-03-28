import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
    
    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                print(message)
            except:
                print("An error occurred!")
                self.socket.close()
                break
    
    def send_message(self):
        while True:
            message = input()
            self.socket.sendall(message.encode('utf-8'))
    
    def run(self):
        receive_thread = threading.Thread(target=self.receive_messages)
        send_thread = threading.Thread(target=self.send_message)
        receive_thread.start()
        send_thread.start()

if __name__ == '__main__':
    chat_client = ChatClient('localhost', 8888)
    chat_client.run()
