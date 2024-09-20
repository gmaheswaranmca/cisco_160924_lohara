import socket
import threading
import json
from search import Search

# Function to handle each client connection
def handle_client(client_socket):
    try:
        # Receive the filename and word from the client
        request = client_socket.recv(1024).decode('utf-8')
        filename, word = request.split(';')  # Split the filename and word sent by the client

        # Search the file for the word
        searcher = Search(filename)
        searcher.clean()
        result = searcher.getLines(word)

        # Send the result back to the client as JSON
        response = json.dumps(result)
        client_socket.send(response.encode('utf-8'))
    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode('utf-8'))
    finally:
        client_socket.close()

def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr}")
        # Handle the client connection in a new thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
