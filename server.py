#Agosto 5, 2024.
# crea la libreria server.py
import socket
#se creara la conexion cliente-servidor
import threading
# todo esto sirve en servidores de aplicaciones (apache tomvat, nginx, JBOSJ, IIs, ...)
def main():
    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #mostrara IPv4 e IPv6, mostrara TCP
    server.bind(('0.0.0.0', 5100)) #localhost, 127.0.0.1 [::1] IP *; puerto 5100
    server.listen(5) #deja 5milisegundos entre llamado y llamado.
    while True:
        print("listening")
         
main()

@>---------------------------------------------------------------------------------------------------
# crea la libreria server.py
import socket
#se creara la conexion cliente-servidor
import threading
# todo esto sirve en servidores de aplicaciones (apache tomvat, nginx, JBOSJ, IIs, ...)
def main():
    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #mostrara IPv4 e IPv6, mostrara TCP
    server.bind(('0.0.0.0', 5100)) #localhost, 127.0.0.1 [::1] IP *; puerto 5100
    server.listen(5) #deja 5milisegundos entre llamado y llamado.
    while True:
        #creacion del hilo administrado por la función cosianfiro
        client.socket, addr = server.accept()
        print(f"connection from {addr} has been established")
        client_handler = threading.Thread(target = handle_client, args = (client_socket, ))
        client_handler.start()

def handle_client(client_socket):
    while True:
        msg = client_socket.recv(1024).decode('utf-8') #1024: tamaño del paquete
        if msg:
            print(f'you: {msg}')
main()

_________--_________--_________--_________--_________--_________--_________
#client.py
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect (('127.0.0.1', 5100))
    while True:
        msg= input ("you")
        client_socket.send(msg.encode('utf-8'))
        
main()
# ya con eso llega un mensaje :D.

"""
powershell
    ipconfig
    10.21.60.x
    10.21.90.x
"""
