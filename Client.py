import socket

def main():
    # Server information
    server_ip = "127.0.0.1"
    server_port = 8080

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to the server at {server_ip}:{server_port}")

    # Get user input for the radius
    radius = float(input("Enter the radius of the sphere: "))

    # Send the radius value to the server
    client_socket.sendall(str(radius).encode())

    # Receive and display the sphere volume from the server
    volume_data = client_socket.recv(1024).decode()
    sphere_volume = float(volume_data)
    print(f"Received sphere volume from server: {sphere_volume}")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
