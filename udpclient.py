import socket #Load the socket module to be able to create a client socket to send data.

# 1️⃣ Creating socket UDP
#AF_INET: uses IPv4 protocol.
#SOCK_DGRAM: defines a datagram (UDP) socket — no connection setup required, just send and receive individual packets.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Create a UDP socket.
#No need to connect(), because UDP sends packets, does not maintain a persistent connection.
# 2️⃣ IP server
server_address = ('127.0.0.1', 12345)
#Specifies the IP and port of the server to which the client will send data.
print("💬 press 'exit' to exit.")#show user to input ' exit' to exit
while True:
    message = input("input message to send to server: ")
    if message.lower() == 'exit':
        break
#Allows the user to enter a message continuously.
#If "exit" is entered, the program ends.
    # 3️⃣ sending data
    client_socket.sendto(message.encode(), server_address)
#Send data to server.
#.encode() converts string to bytes.
#Since UDP is connectionless, each time you send, you need to specify the destination address (server_address).
    # 4️⃣ receiving response
    data, _ = client_socket.recvfrom(1024)
    print(f"🔁 response from server: {data.decode()}") #Print the response received from the server.
#Wait for a response from the server.
#_ is used to ignore the source address because we already know the response is coming from the server.
client_socket.close()
#Close the client socket after the user exits.