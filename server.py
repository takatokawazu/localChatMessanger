import socket
from faker import Faker


def main():
    host = "localhost"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening on port", port)

    faker = Faker()

    while True:
        client_socket, client_addr = server_socket.accept()
        print("Connected by", client_addr)

        data = client_socket.recv(1024).decode()
        if not data:
            break

        print("Received message:", data)

        # Generate a fake response using faker
        fake_response = faker.sentence()
        client_socket.send(fake_response.encode())

        client_socket.close()


if __name__ == "__main__":
    main()
