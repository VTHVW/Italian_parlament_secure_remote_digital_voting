from threading import Thread
import json

class client(Thread):
    def __init__(self,conn,addr,logger,event,database):
        self.conn = conn
        self.addr = addr
        self.logger = logger
        self.event = event
        self.db = database
        Thread.__init__(self)

    def run(self):
        global are_voting
        global vote_type
        self.logger.debug("New thread running")
        while True:
            if are_voting == True:
                self.conn.send("voting".encode())
            else:
                self.conn.send("not voting".encode())
                self.event.wait()
                self.conn.send("voting".encode())
                if vote_type == "palese":
                    vote = self.conn.recv(1024).encode()
                else:
                    vote = self.conn.recv(1024).encode()
