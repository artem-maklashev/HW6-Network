import socket
import threading
from time import sleep

nickname = input("Введите свой ник: ")
addr = ("127.0.0.1", 55555)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def recive():
    while True:
        try: 
            message = client.recv(1024).decode("utf-8")
            if message == 'Nick':
                client.send(nickname.encode("utf-8"))
            else :
                print(message)
        except:
             print("Ошибка")
             client.close()
             break
def send_mes():
        while True:
             message = '{}'.format(input(''))
             client.send(message.encode("utf-8"))

    
        
rec_thread = threading.Thread(target=recive)
rec_thread.start()
out_thread = threading.Thread(target = send_mes)
out_thread.start()


# Ждем, пока поток recive завершит работу или пройдет определенное количество времени
# rec_thread.join(timeout=4)

# if data_received_event.is_set():
#     print(data_in)
# else:
#     send_mes()
# while True:
#     try:
#         message = recive()
#         if not message:
#                break
        
#         send_mes()
#     except Exception as e:  
#         print(f"Ошибка при обработке клиента: {e}")
#         break

# socket_call.close()
