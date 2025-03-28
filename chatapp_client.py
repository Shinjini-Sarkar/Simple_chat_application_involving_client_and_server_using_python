import socket

def start_client():
    ADD=socket.gethostbyname(socket.gethostname())
    PORT=5050

    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #connect the client socket to server of ADD and PORT
    client_socket.connect((ADD,PORT))
    print("Connected to the server. Type exit to disconnect. ")

    while True:
        client_msg=input("YOU: ")
        client_socket.send(client_msg.encode())
        if(client_msg.lower()=='exit'):
           print("Client exitting")
           break
        server_msg=client_socket.recv(1024).decode()
        if(server_msg.lower()=='exit'):
            print("Server quitting")
            break
        print(f"Server: {server_msg}")

    client_socket.close()

if __name__ == "__main__":
    start_client()