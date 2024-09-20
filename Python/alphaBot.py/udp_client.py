import socket

# Dati del server (indirizzo IP e porta)
server_address = ("172.20.10.3", 6980)  # Inserire l'indirizzo IP del server e la porta; localhost = indirizzo ip del server
BUFFER_SIZE = 4096  # Dimensione massima del buffer per la ricezione dei dati

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Messaggio
message = "Ciao Cava, sono Fant!"
udp_client_socket.sendto(message.encode(), server_address)

data, server = udp_client_socket.recvfrom(BUFFER_SIZE)
print(f"Risposta dal server: {data.decode()}")

udp_client_socket.close()