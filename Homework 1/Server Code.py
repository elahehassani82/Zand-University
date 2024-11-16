import socket

def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server to listen on port 12345
    server_socket.bind(('0.0.0.0', 12345))  # Listen on port 12345 on all available network interfaces
    server_socket.listen(1)  # Allow only one connection at a time
    
    print("Server is listening on port 12345...")
    
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}.")
    
    # Receive and send messages in a loop
    while True:
        message = client_socket.recv(1024).decode()  # Receive message from the client
        if message.lower() == 'exit':
            print("Connection closed.")
            break
        print(f"Client: {message}")
        
        response = input("You: ")  # Ask the server user to input a message
        client_socket.send(response.encode())  # Send the response to the client
    
    # Close the sockets
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
