import socket
import threading

def handle_client(client_socket, addr):
    print(f"Connection from {addr} has been established.")
    
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:  # Nếu không có tin nhắn nào, thoát vòng lặp
            break
        print(f"Received message: {message}")
        
        response = f"Server received: {message}"
        client_socket.send(response.encode('utf-8'))
    
    client_socket.close()
    print(f"Connection from {addr} has been closed.")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 12347))
    server_socket.listen(5)  # Cho phép tối đa 5 kết nối chờ
    print("Server is listening on port 12346...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            # Tạo một luồng mới để xử lý client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()  # Đảm bảo socket được đóng khi server dừng

if __name__ == "__main__":
    start_server()
