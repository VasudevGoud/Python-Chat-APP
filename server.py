import socket
import threading


HEADER=64   #bytes
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,  PORT )
FORMAT= 'utf-8'
DISCONNECT_MESSAGE= 'DISCONNECT !'
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[new connection]{addr} connected")

    connected= True
    while connected:
      try:
        msg_length=conn.recv(HEADER).decode()
        msg_length=int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {msg}")
        if msg==DISCONNECT_MESSAGE:
            connected=False
      except:
        break
        
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
        

    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr=server.accept()
        thread=threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")


print("[STARTING] server is  starting...")
start()