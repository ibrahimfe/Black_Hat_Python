import socket

target_host = "www.google.com"
target_port = 80

# create a socket object =
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the client
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\n Host: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()