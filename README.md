# Python Socket Chat Application

## Overview
The **Python Socket Chat Application** is a simple client-server chat system built using Python's socket programming. It enables two-way communication between a client and a server over a local network. The application consists of two files:
- `chatapp_server.py` - Runs the server that listens for incoming client connections.
- `chatapp_client.py` - Connects to the server and allows message exchange.

## Features
- Real-time messaging between client and server.
- Ability to send and receive messages in a continuous loop.
- Users can type `exit` to disconnect from the chat.
- Uses **TCP sockets** for reliable communication.

## Technologies Used
- **Programming Language:** Python
- **Networking:** Python `socket` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Shinjini-Sarkar/Simple_chat_application_involving_client_and_server_using_python/tree/main
   ```
2. Navigate to the project folder:
   ```sh
   cd PYTHON_CHATAPP
   ```
3. Ensure you have Python installed (version 3.x recommended).

## Usage

### Running the Server
1. Open a terminal or command prompt.
2. Navigate to the project directory and run:
   ```sh
   python chatapp_server.py
   ```
3. The server will start and wait for a client to connect.

### Running the Client
1. Open another terminal or command prompt.
2. Navigate to the project directory and run:
   ```sh
   python chatapp_client.py
   ```
3. Once connected, you can start sending messages.
4. Type `exit` to close the connection.

## Project Structure
```
PYTHON_CHATAPP/
│── chatapp_client.py    # Client-side script
│── chatapp_server.py    # Server-side script
│── README.md    # Project documentation
```

## Troubleshooting
- Ensure both the **server** and **client** are running in separate terminals.
- Make sure no other process is using port `5050`.
- If the connection fails, check your **firewall settings** or **IP address**.
