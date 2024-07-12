import socket


def main():
    # IP dan port yang digunakan server
    server_ip = "127.0.0.1"  # Sesuaikan dengan IP server jika server tidak berjalan di localhost
    server_port = 9998  # Sesuaikan dengan port server

    # Buat socket untuk koneksi ke server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Lakukan koneksi ke server
        client.connect((server_ip, server_port))
        print(f"[*] Connected to {server_ip}:{server_port}")

        # Kirimkan data ke server
        message = "Hello, Server!"
        client.send(message.encode("utf-8"))

        # Terima respon dari server
        response = client.recv(4096)
        print(f"[*] Received: {response.decode('utf-8')}")

    except Exception as e:
        print(f"[!] Error: {e}")

    finally:
        # Tutup koneksi
        client.close()


if __name__ == "__main__":
    main()
