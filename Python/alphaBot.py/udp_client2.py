import socket
import time  # per inserire un breve ritardo tra i messaggi

server_address = ("127.0.0.1", 6980)  #  IP del server e la porta
BUFFER_SIZE = 4096 
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creazione socket UDP del client

# Invia 10 messaggi consecutivi al server
for i in range(1, 11):
    # Messaggio da inviare
    message = f"Messaggio {i} dal Client!"
    print(f"Invio: {message}")
    
    udp_client_socket.sendto(message.encode(), server_address)    # invio messaggio al server
    
    # Riceve la risposta dal server
    data, server = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f"Risposta dal server: {data.decode()}")
    
    time.sleep(1)

# Chiusura del socket 
udp_client_socket.close()