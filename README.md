
# Python Chat App 

A basic terminal-based chat application built with Python using sockets and multithreading. This project demonstrates how a server can handle multiple clients at once, allowing real-time message broadcasting among all connected users. It's a simple yet effective way to learn and understand the fundamentals of network communication in Python.

## Features

- Multithreaded server handling multiple clients
- Basic message broadcasting to all clients
- Graceful client disconnection
- Easily extendable structure

## Files

- `server.py` — The server script that accepts client connections and handles message broadcasting.
- `client.py` — The client script that connects to the server and sends/receives messages.

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/VasudevGoud/Python-Chat-APP.git
cd Python-Chat-APP
```

### 2. Run the Server

In one terminal window:

```bash
python3 server.py
```

This starts the server and begins listening for incoming connections.

### 3. Run a Client

In another terminal window:

```bash
python3 client.py
```

You can open multiple terminals to simulate multiple clients.

## Usage

- Type a message and hit Enter to send it.
- To disconnect, type:

```
DISCONNECT !
```

## Requirements

- Python 3.x

This app uses only Python's built-in libraries (`socket`, `threading`), so no extra dependencies are required.

## Author

- [VASUDEV GOUD BIKKI]
```
