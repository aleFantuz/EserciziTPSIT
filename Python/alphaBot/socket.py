# import socket

# #SERVER

# server_address = ("localhost",6980)  #localhost = indirizzo ip del server
# BUFFER_SIZE = 4092
# udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #tira su il server socket
# udp_server_socket.bind(server_address) #faccio il bind con il server socket

# data, address = udp_server_socket.recvfrom(BUFFER_SIZE) #mette in ascolto , bloccante

# print(f"Messaggio ricevuto: {data.decode()} da {address}")  # uso decode() per decoficare la data

# #CLIENT
# #creo messaggio 
# try:
#     udp_server_socket.sendto(message, server_address)
#     data, address = udp_server_socket.recvfrom(BUFFER_SIZE)