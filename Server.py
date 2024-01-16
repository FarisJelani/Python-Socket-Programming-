import socket
import math

def calculate_sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def main():
    # Server information
    server_ip = "192.168.75.132"
    server_port = 8080

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Receive the radius value from the client
        radius_data = client_socket.recv(1024)
        if not radius_data:
            break

        # Calculate sphere volume
        radius = float(radius_data.decode())
        volume = calculate_sphere_volume(radius)

        # Send the calculated volume back to the client
        client_socket.sendall(str(volume).encode())

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    main()
