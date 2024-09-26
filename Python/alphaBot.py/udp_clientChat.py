import socket

server_address = ("127.0.0.1", 6980)  # inserisco IP del server(computer dell'altro) e la porta
BUFFER_SIZE = 4096  # Dimensione massima del buffer per la ricezione dei dati

# Creazione socket UDP del client
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Invio di un messaggio al server
    message = input("Inserisci il messaggio da inviare al server: ")
    udp_client_socket.sendto(message.encode(), server_address)

    # Se il messaggio è "exit", chiudi la connessione
    if message.lower() == "exit":
        print("Chiusura del client...")
        udp_client_socket.close()
        break

    # Ricezione della risposta dal server
    data, server = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f"Risposta dal server: {data.decode()}")