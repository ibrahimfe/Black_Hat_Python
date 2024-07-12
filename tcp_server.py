import socket
import threading

# IP and Port the server listen to
IP = "0.0.0.0"
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))  # Masukan ip dan port ke dalam server
    server.listen(
        5
    )  # menyuruh server untuk listen atas request dengan maksimal back log request nya 5
    print(f"[*] Listening on {IP} : {PORT}")

    # loop untuk membuat server selalu menerima request
    while True:
        client, address = server.accept()  # receive the client socket
        print(f"[*] Accepted Connection from {address[0]:{address[1]}}")
        # handle koneksi dari client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(clien_socket):
    with clien_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b"ACK")


if __name__ == "__main__":
    main()
