import socket
import json

def start_client(filename, word, host='127.0.0.1', port=65432):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
        # Send the filename and word to the server in the format: filename;word
        request = f"{filename};{word}"
        client.send(request.encode('utf-8'))

        # Receive the result from the server
        response = client.recv(4096).decode('utf-8')

        # Parse the JSON response
        result = json.loads(response)
        print("Search Results:", result)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    word = input("Enter the word to search: ")
    start_client(filename, word)