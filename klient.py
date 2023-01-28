# Чат клієнт повідомлення з консолі
import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

msg1 = input("Enter a message for the server: ")

sock.send(pickle.dumps(msg1))
data = sock.recv(1024)
answer = pickle.loads(data)
print(answer)
sock.close()