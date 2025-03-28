import socket

def start_server():

    ADD=socket.gethostbyname(socket.gethostname())
    PORT=5050

    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((ADD,PORT))
    server_socket.listen(1) # listen 1 connection at a time

    print("Server Started. Waiting for connection... ")
    conn,addr=server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        #server receives msg from client

           client_msg=conn.recv(1024).decode()
           if client_msg.lower()=='exit':
              print("Client disconnected")
              break
           print(f"Client:{client_msg}")

        #server sends msg to client
           server_msg=input("YOU: ")
           conn.send(server_msg.encode())
           if server_msg=='exit':
              print("Server is quitting")
              break
    conn.close()
if __name__ == "__main__":
    start_server()