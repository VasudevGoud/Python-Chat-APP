import socket

HEADER=64   #bytes
PORT=5050

FORMAT= 'utf-8'
DISCONNECT_MESSAGE= 'DISCONNECT !'
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))  # Padding to fit HEADER size
    client.send(send_length)
    client.send(message)

# Test messages
send("Hello Server!")
send("This is a test message.")
send(DISCONNECT_MESSAGE)