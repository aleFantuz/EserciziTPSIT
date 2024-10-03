import socket

server_address = ("172.20.10.2", 6980)  # inserisco IP del server(computer dell'altro) e la porta
BUFFER_SIZE = 4096  # Dimensione massima del buffer per la ricezione dei dati

# Creazione socket UDP del client
print("fff")
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # messaggio al server
    message = input("Inserisci il messaggio da inviare al server: ")
    udp_client_socket.sendto(message.encode(), server_address)

    if message.lower() == "exit":
        print("Chiusura del client...")
        udp_client_socket.close()
        break

    # Ricezione della risposta dal server
    data, server = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f"Risposta dal server: {data.decode()}")