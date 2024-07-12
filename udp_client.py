import socket


def main():
    # IP dan port yang digunakan server
    server_ip = "127.0.0.1"  # Sesuaikan dengan IP server jika server tidak berjalan di localhost
    server_port = 9998  # Sesuaikan dengan port server

    # Buat socket untuk koneksi UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Kirimkan data ke server
        message = "Hello, Server!"
        client.sendto(message.encode("utf-8"), (server_ip, server_port))
        print(f"[*] Sent: {message}")

        # Terima respon dari server
        response, server = client.recvfrom(4096)
        print(f"[*] Received from {server}: {response.decode('utf-8')}")

    except Exception as e:
        print(f"[!] Error: {e}")

    finally:
        # Tutup koneksi
        client.close()


if __name__ == "__main__":
    main()
