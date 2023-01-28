# Чат сервер повідомлення з консолі
import socket
import pickle
import logging

module_logger = logging.getLogger("exampleApp.server")

def serv():


    module_logger.info('Start module server')
    logger = logging.getLogger("exampleApp.serv")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 55000))

    sock.listen(10)
    logger.info(f"Server is running")
    print('Server is running, please, press ctrl+c to stop')

    conn, addr = sock.accept()
    logger.info(f"'connected:', {addr}")
    data = conn.recv(1024)
    data = pickle.loads(data)
    print(data)
    logger.info(f"'Data received:', {data}")

    msg1 = input("Enter a message for the klient: ")
    logger.info(f"'Data entered for the klient:', {msg1}")
    conn.send(pickle.dumps(msg1))
    logger.info(f"'Data sent:', {msg1}")
    conn.close()
    module_logger.info('End module server')





