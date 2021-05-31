import signal
import time
import sys

from pirc522 import RFID

def block_to_str(data):
    return bytes(data).decode().replace('\x00','')

class Reader():
    def __init__(self,key_a=[0x01,0x02,0x03,0x04,0x05,0x06],key_b=[0x06, 0x05, 0x04, 0x03, 0x02, 0x01]):
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = True
        signal.signal(signal.SIGINT, self.end_read)
        self.id_block=0
        self.name_block=1
        self.surname_block=2
        self.sector=1
        self.key_a=key_a
        self.key_b=key_b

    def end_read(self,signal=None,frame=None):
        self.rdr.stop_crypto()
        #  self.rdr.cleanup()

    def read_id(self):
        block_data = None
        self.rdr.wait_for_tag()

        (error, data) = self.rdr.request()
        if not error:
            (error, uid) = self.rdr.anticoll()
            if not error:
                sector = self.sector
                block = self.id_block
                if not self.rdr.select_tag(uid):
                    if not self.rdr.card_auth(self.rdr.auth_b, sector*4+block, self.key_b, uid):
                        _ , block_data = self.rdr.read(sector*4+block)
                    else:
                        self.end_read()
                        raise Exception("Impossible to auth tag")
                else:
                    self.end_read()
                    raise Exception("Impossible to select tag")
                self.end_read()
                return block_data
            else:
                self.end_read()
                raise Exception("Error during anti collision algorithm")
        else:
            self.end_read()
            raise Exception("Error during tag request")

    def read_name(self):
        block_data = None
        self.rdr.wait_for_tag()

        (error, data) = self.rdr.request()
        if not error:
            (error, uid) = self.rdr.anticoll()
            if not error:
                sector = self.sector
                block = self.name_block
                if not self.rdr.select_tag(uid):
                    if not self.rdr.card_auth(self.rdr.auth_b, sector*4+block, self.key_b, uid):
                        _ , block_data = self.rdr.read(sector*4+block)
                    else:
                        self.end_read()
                        raise Exception("Impossible to auth tag")
                else:
                    self.end_read()
                    raise Exception("Impossible to select tag")
                self.end_read()
                return block_data
            else:
                self.end_read()
                raise Exception("Error during anti collision algorithm")
        else:
            self.end_read()
            raise Exception("Error during tag request")


    def read_surname(self):
        block_data = None
        self.rdr.wait_for_tag()

        (error, data) = self.rdr.request()
        if not error:
            (error, uid) = self.rdr.anticoll()
            if not error:
                sector = self.sector
                block = self.surname_block
                if not self.rdr.select_tag(uid):
                    if not self.rdr.card_auth(self.rdr.auth_b, sector*4+block, self.key_b, uid):
                        _ , block_data = self.rdr.read(sector*4+block)
                    else:
                        self.end_read()
                        raise Exception("Impossible to auth tag")
                else:
                    self.end_read()
                    raise Exception("Impossible to select tag")
                self.end_read()
                return block_data
            else:
                self.end_read()
                raise Exception("Error during anti collision algorithm")
        else:
            self.end_read()
            raise Exception("Error during tag request")

    def read_all(self):
        return (self.read_id(),self.read_name(),self.read_surname())

    def read_all_str(self):
        return (self.read_id(),block_to_str(self.read_name()),block_to_str(self.read_surname()))


class Writer():
    def __init__(self,key_a=[0x01,0x02,0x03,0x04,0x05,0x06],key_b=[0x06, 0x05, 0x04, 0x03, 0x02, 0x01]):
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = True
        signal.signal(signal.SIGINT, self.end_read)
        self.id_block=0
        self.name_block=1
        self.surname_block=2
        self.sector=1
        self.key_a=key_a
        self.key_b=key_b

    def end_read(self,signal=None,frame=None):
        self.rdr.stop_crypto()
        #  self.rdr.cleanup()

    def write_id(self,id):
        self.rdr.wait_for_tag()

        (error, data) = self.rdr.request()
        if not error:
            (error, uid) = self.rdr.anticoll()
            if not error:
                sector = self.sector
                block = self.id_block
                if not self.rdr.select_tag(uid):
                    if not self.rdr.card_auth(self.rdr.auth_b, sector*4+block, self.key_b, uid):
                        self.rdr.write(sector*4+block,id[:16])
                    else:
                        self.end_read()
                        raise Exception("Impossible to auth tag")
                else:
                    self.end_read()
                    raise Exception("Impossible to select tag")
                self.end_read()
            else:
                self.end_read()
                raise Exception("Error during anti collision algorithm")
        else:
            self.end_read()
            raise Exception("Error during tag request")

    def write_name(self,name):
        self.rdr.wait_for_tag()

        (error, data) = self.rdr.request()
        if not error:
            (error, uid) = self.rdr.anticoll()
            if not error:
                sector = self.sector
                block = self.name_block
                if not self.rdr.select_tag(uid):
                    if not self.rdr.card_auth(self.rdr.auth_b, sector*4+block, self.key_b, uid):
                        data= list(name.encode()[:16])
                        while len(data)<16:
                            data += [0x00]
                        self.rdr.write(sector*4+block, data)
                    else:
                        self.end_read()
                        raise Exception("Impossible to auth tag")
                else:
                    self.end_read()
                    raise Exception("Impossible to select tag")
                self.end_read()
            else:
                self.end_read()
                raise Exception("Error during anti collision algorithm")
        else:
            self.end_read()
            raise Exception("Error during tag request")


    def write_surname(self,surname):
        self.rdr.wait_for_tag()

        (error, data) = self.rdr.request()
        if not error:
            (error, uid) = self.rdr.anticoll()
            if not error:
                sector = self.sector
                block = self.surname_block
                if not self.rdr.select_tag(uid):
                    if not self.rdr.card_auth(self.rdr.auth_b, sector*4+block, self.key_b, uid):
                        data= list(surname.encode()[:16])
                        while len(data)<16:
                            data += [0x00]
                        self.rdr.write(sector*4+block, data)
                    else:
                        self.end_read()
                        raise Exception("Impossible to auth tag")
                else:
                    self.end_read()
                    raise Exception("Impossible to select tag")
                self.end_read()
            else:
                self.end_read()
                raise Exception("Error during anti collision algorithm")
        else:
            self.end_read()
            raise Exception("Error during tag request")

    def write_all(self,id,name,surname):
        self.write_id(id)
        self.write_name(name)
        self.write_surname(surname)
