import socket
import logging
import database_thread
import thread_connection
from threading import Event
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

database = database_thread.votazioni_thread()

event = Event()

ip = "127.0.0.1"
port = 47474

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip,port))
logger.debug("Socket binded")

sock.listen()
logger.info("Server Listening...")

while True:
    conn, addr = sock.accept()
    if addr[0] == "127.0.0.1":
        logger.info(f"New amministrator connection {addr}")
        thread_connection.admin(conn,addr,logger,event,database)
    else:
        logger.info(f"New connection {addr}")
        thread_connection.client(conn,addr,logger,event,database)
