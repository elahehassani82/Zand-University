import socket

def start_client():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server using its IP address and port 12345
    server_ip = input("Enter the server IP address: ")
    client_socket.connect((server_ip, 12345))  # Connect to the server on port 12345
    
    print("Connection established. Type 'exit' to quit.")
    
    # Send and receive messages in a loop
    while True:
        message = input("You: ")  # Ask the client user to input a message
        client_socket.send(message.encode())  # Send the message to the server
        
        if message.lower() == 'exit':  # If 'exit' is typed, break the loop
            print("Connection closed.")
            break
        
        response = client_socket.recv(1024).decode()  # Receive the server's response
        print(f"Server: {response}")
    
    # Close the socket
    client_socket.close()

ifuser to in== "__main__":
    start_client()
