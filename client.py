import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Socket config
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT !"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Send message to server
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

# GUI functions
def send_message():
    msg = msg_entry.get()
    if msg:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"You: {msg}\n")
        chat_box.config(state=tk.DISABLED)
        send(msg)
        msg_entry.delete(0, tk.END)
        if msg == DISCONNECT_MESSAGE:
            root.destroy()

# GUI setup
root = tk.Tk()
root.title("Python Chat Client")
root.geometry("400x500")

chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

msg_entry = tk.Entry(root, font=("Arial", 14))
msg_entry.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Start the GUI loop
root.mainloop()
