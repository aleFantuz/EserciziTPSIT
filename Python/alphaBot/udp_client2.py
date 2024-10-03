import socket
server_address = ("172.20.10.", 6980)  #  IP del server e la porta
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creazione socket UDP del client

#  invio dei messaggi
try:    
    for i in range(1, 11):
        # Messaggio da inviare
        message = f"Messaggio {i} dal Client!"
        print(f"Invio: {message}")

        udp_client_socket.sendto(message.encode(), server_address)    # invio messaggio al server

        # Riceve la risposta dal server
        data, server = udp_client_socket.recvfrom(4096)
        print(f"Risposta dal server: {data.decode()}")

finally:

# Chiusura del socket 
    udp_client_socket.close()






    #socket tcp --> gestione di connessione , gestione degli errori

    #                    #-----------TCP------------#
    # tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # {
    #     tcp_server_socket.bind(server_address)      // per il server
    #     tcp_client_socket.connect(server_address)    //per il client
    # }

    # tcp_server_socket.listen(1)   //dimensione della coda di connessioni
    # conn, address = tcp_server_socket.accept()   #bloccante, mette il server in ascolto
    # conn.sendall(b"Messaggio ricevuto")  // sempre per il server 
    # 1- forwars
    # 2-backward
    # 3-right
    # 4-left
    # value-> 0 / 100 (da 0 a 100)
    
    # SERVER:
    # "1,55"