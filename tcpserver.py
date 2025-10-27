import socket #Load the socket module to create and manage network connections.

# 1️⃣ Creating socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET: use IPv4.
#SOCK_STREAM: defines this as a TCP (stream-oriented) socket – data is transmitted in a continuous, reliable stream.
# 2️⃣ Assign IP and port
server_address = ('127.0.0.1', 12346)#127.0.0.1: localhost – meaning it will only run on your computer, 12346: the port where the server will “listen” for connection requests.
server_socket.bind(server_address)#bind() makes the socket bind to this address.
server_socket.listen(1)## allow 1 client to connect
print("✅ TCP Server is waiting to connect...")
#Put the socket into “listen” mode (listen()): the server is ready to receive clients.
# 3️⃣ Accept connections from clients
connection, client_address = server_socket.accept()
print(f"📶 Connected from: {client_address}")
#When a client calls connect(), the server establishes a separate connection.
#Returns 2 values: connection: a new socket dedicated to that client. client_address: the address (IP, port) of the client.
# 4️⃣ Receive/Send Loop
while True:#The loop continues processing as the client sends data.
    data = connection.recv(1024)
    if not data:
        break
    print(f"📩 Receicving from client: {data.decode()}")#Print the received content.
    connection.sendall(data)  #sendall() sends all data back to the client (Echo).
#recv(1024) receives a maximum of 1024 bytes of data.
#When the client closes the connection, the data will be empty (not data) → exit the loop.
#Unlike UDP: TCP does not need to specify an address, because the connection is already established.
connection.close()
server_socket.close()
print("🔒 Connection closed.")
#Close the connection to the client, then shut down the server socket.
#Free up network resources.