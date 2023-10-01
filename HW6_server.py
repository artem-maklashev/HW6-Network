import socket
import threading

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем адрес и порт для прослушивания
host = "127.0.0.1"  # IP-адрес сервера
port = 55555       # Порт сервера

# Привязываем соксет к адресу и порту
server_socket.bind((host, port))

# Начинаем прослушивание (ожидание клиентских подключений)
server_socket.listen(5)  # 5 - максимальное количество ожидающих клиентов в очереди

print(f"Сервер слушает на {host}:{port}")

# Список клиентских соединений и их никнеймов
clients = []
def handle_client(client_socket):
    # Отправляем запрос на никнейм
    client_socket.send('Nick'.encode("utf-8"))

    # Принимаем никнейм от клиента
    nickname = client_socket.recv(1024).decode("utf-8")
    if not nickname:
        raise ValueError("Неверный никнейм")
    print(f"Принято соединение с {nickname}")

    # Добавляем клиента в список
    clients.append((client_socket, nickname))

    while True:
        try:
            # Принимаем сообщение от клиента
            message = client_socket.recv(1024).decode("utf-8")
            print(f"пришло сообщение {message}")
            if not message:
                break

            # Отправляем сообщение всем подключенным клиентам
            for (client, _) in clients:
                if client != client_socket:
                    client.send(f"{nickname}: {message}".encode("utf-8"))
        except Exception as e:
            print(f"Ошибка при обработке клиента: {e}")
            break

    
    # Удаляем клиента из списка и закрываем соединение
    clients.remove((client_socket, nickname))
    client_socket.close()

while True:
    # Принимаем подключение от клиента
    client_socket, client_address = server_socket.accept()

    # Запускаем поток для обработки клиента
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
