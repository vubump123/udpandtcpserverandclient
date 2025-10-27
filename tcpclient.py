import socket #Load the socket module to create and manage network connections.

# 1️⃣ Create TCP sockets for connected data transmission.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2️⃣ connect to server
server_address = ('127.0.0.1', 12346)
client_socket.connect(server_address)
print("💬 Connected to server (TCP). Type 'exit' to exit.") #Confirm connection successful.
#Here the 3-way handshake takes place:
#Client sends SYN, Server sends SYN-ACK,Client sends ACK → connection ready.
while True:
    message = input("Enter message to send to server: ")
    if message.lower() == 'exit':
        break
#Loop allows user to send multiple messages.
#Type "exit" → end the program.
    client_socket.sendall(message.encode())  # send data,
    data = client_socket.recv(1024)          # receive feedback
    print(f"🔁 Response from server: {data.decode()}")
#Send data over a (connected) TCP channel.
#sendall() guarantees to send the entire data, even if it has to be split into multiple packets.
#.encode() converts string → bytes to send.
#Receive response from server.
#recv() blocks until data is received.
#.decode() to display data in text format.
client_socket.close()
#Close TCP connection, release resources.