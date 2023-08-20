import socket


def main():
    host = "localhost"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter a message: ")
        if message.lower() == "exit":
            break

        client_socket.send(message.encode())

        response = client_socket.recv(1024)
        print("Server response:", response.decode())

    client_socket.close()


if __name__ == "__main__":
    main()
