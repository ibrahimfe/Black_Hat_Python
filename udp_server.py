import socket

# IP dan Port yang digunakan server
IP = "0.0.0.0"
PORT = 9998


def main():
    # Buat socket untuk koneksi UDP
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind socket ke IP dan port yang telah ditentukan
    server.bind((IP, PORT))

    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        # Terima data dari client
        data, address = server.recvfrom(4096)
        print(f"[*] Received from {address}: {data.decode('utf-8')}")

        # Kirimkan respon ke client
        server.sendto(b"ACK", address)


if __name__ == "__main__":
    main()
