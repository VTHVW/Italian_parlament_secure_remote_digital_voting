from database import Votazioni
import threading as t

class votazioni_thread(Votazioni):
    def __init__(self):
        super().__init__(self)
        self.lock = t.Lock()

    def set_id(self, id):
        self.lock.acquire()
        try:
            super().set_id(id)
        finally:
            self.lock.release()


    def add_vote(self, vote, name, id = None):
        self.lock.acquire()
        try:
            super().add_vote(vote,nome,id)
        finally:
            self.lock.release()

