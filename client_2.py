#client_2.py
import socket
import os

def send_file(file_path):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    # Send file name
    file_name = os.path.basename(file_path)
    client.send(file_name.encode('utf-8'))

    # Send file data
    with open(file_path, 'rb') as file:
        while True:
            bytes_read = file.read(1024)
            if not bytes_read:
                break
            client.sendall(bytes_read)

    print(f"File {file_name} sent successfully.")
    client.close()

if __name__ == "__main__":
    file_path = input("Enter the path of the file to send: ")
    send_file(file_path)
  -------------------------------------------------------------------------------------------
#server_2.py
import socket

def receive_file():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen()
    print("Server listening on port 5555...")

    client_socket, address = server.accept()
    print(f"Connection from {address} has been established.")

    # Receive file name
    file_name = client_socket.recv(1024).decode('utf-8')
    print(f"Receiving file: {file_name}")

    # Receive file data
    with open(file_name, 'wb') as file:
        while True:
            bytes_read = client_socket.recv(1024)
            if not bytes_read:    
                break
            file.write(bytes_read)

    print(f"File {file_name} received successfully.")
    client_socket.close()
    server.close()

if __name__ == "__main__":
    receive_file()
