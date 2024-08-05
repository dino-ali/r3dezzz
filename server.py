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
