import socket #Load Python's socket module to be able to create network connections.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET: uses IPv4 protocol.
#SOCK_DGRAM: defines a datagram (UDP) socket — no connection setup required, just send and receive individual packets.
# 2️⃣ Assign IP address and port

server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)
#127.0.0.1 is localhost, meaning the server only listens on your machine.
#12345 is the port number for the client to send data to.
#bind() helps the socket "attach" to this address to be ready to receive data
print("✅ UDP Server is running... (press ctrl+c to stop)")
#Print a message to the screen indicating that the server has started and is waiting to receive packets.
# 3️⃣ Repeat: receive and resend data
while True:
    data, client_address = server_socket.recvfrom(1024)  # receive up to 1024 bytes
    print(f"📩 receive from {client_address}: {data.decode()}") #.decode() converts bytes to a string for readable display.
    server_socket.sendto(data, client_address)  # Send the correct received content (Echo) back to the client.
    #sendto() in UDP requires both the data and the destination address to be sent.
    #This way the client knows the server has responded.

#Loop indefinitely so that the server is always ready to process incoming packets.
#recvfrom(1024) receives a maximum of 1024 bytes of data.
#This command returns 2 values:
#data: the content that the client sends.
#client_address: tuple containing (IP, port) of the client sending the data.