from pirc522 import RFID

data_position = {"sector_data":1,"block_data":{"id":0,"name":1,"surname":2}}

class RFID_Writer():
    def __init__(self,id,name,surname,keys=([0x01,0x02,0x03,0x04,0x05,0x06],[0x06,0x05,0x04,0x03,0x02,0x01])):
        self.id = id
        self.name = name
        self.surname = surname
        self.key_a = keys[0]
        self.key_b = keys[1]
        self.rdr = RFID()
        self.util = self.rdr.util()
        #  self.util.debug = True

    def write_id(self,id):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if error:
            raise Exception("Error detecting the tag")
        (error, uid) = self.rdr.anticoll()
        if error:
            raise Exception("Error in anti collision algorithm")

        global data_position
        sector = data_position["sector_data"]
        block = data_position["block_data"]["id"]
        if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
            self.rdr.write(sector*4+block, id[:16])

        self.rdr.cleanup()
        self.util.deauth()

    def write_name(self,name):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if error:
            raise Exception("Error detecting the tag")
        (error, uid) = self.rdr.anticoll()
        if error:
            raise Exception("Error in anti collision algorithm")

        global data_position
        sector = data_position["sector_data"]
        block = data_position["block_data"]["name"]
        if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
            self.rdr.write(sector*4+block, name.encode()[:16])

        self.rdr.cleanup()
        self.util.deauth()

    def write_surname(self,surname):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if error:
            raise Exception("Error detecting the tag")
        (error, uid) = self.rdr.anticoll()
        if error:
            raise Exception("Error in anti collision algorithm")

        global data_position
        sector = data_position["sector_data"]
        block = data_position["block_data"]["surname"]
        if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
            self.rdr.write(sector*4+block, surname.encode()[:16])

        self.rdr.cleanup()
        self.util.deauth()

    def write_all(self,id,name,surname):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if error:
            raise Exception("Error detecting the tag")
        (error, uid) = self.rdr.anticoll()
        if error:
            raise Exception("Error in anti collision algorithm")

        global data_position
        sector = data_position["sector_data"]
        block_data = {data_position["block_data"]["id"]:id,data_position["block_data"]["name"]:name.encode(),data_position["block_data"]["surname"]:surname.encode()}
        for block, data in block_data.items():
            if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
                self.rdr.write(sector*4+block, data[:16])

        self.rdr.cleanup()
        self.util.deauth()


class RFID_Reader():
    def __init__(self,keys=([0x01,0x02,0x03,0x04,0x05,0x06],[0x06,0x05,0x04,0x03,0x02,0x01])):
        self.key_a = keys[0]
        self.key_b = keys[1]
        self.rdr = RFID()
        self.util = self.rdr.util()
        #  self.util.debug = True

    def read_id(self):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if not error:
            (error, uid) = self.rdr.anticoll()
            if not error:
                global data_position
                sector = data_position["sector_data"]
                block = data_position["block_data"]["id"]
                res_data = None
                if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
                    _, res_data = self.rdr.read(sector*4+block)

                self.rdr.cleanup()
                self.util.deauth()

                return res_data
            else:
                raise Exception("Error in anti collision algorithm")
        else:
            raise Exception("Error detecting the tag")

    def read_name(self):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if error:
            raise Exception("Error detecting the tag")
        (error, uid) = self.rdr.anticoll()
        if error:
            raise Exception("Error in anti collision algorithm")

        global data_position
        sector = data_position["sector_data"]
        block = data_position["block_data"]["name"]
        res_data = None
        if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
            _, res_data = self.rdr.read(sector*4+block)

        self.rdr.cleanup()
        self.util.deauth()

        return res_data

    def read_surname(self):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if error:
            raise Exception("Error detecting the tag")
        (error, uid) = self.rdr.anticoll()
        if error:
            raise Exception("Error in anti collision algorithm")

        global data_position
        sector = data_position["sector_data"]
        block = data_position["block_data"]["surname"]
        res_data = None
        if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
            _, res_data = self.rdr.read(sector*4+block)

        self.rdr.cleanup()
        self.util.deauth()

        return res_data

    def read_all(self):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()

        if error:
            raise Exception("Error detecting the tag")
        (error, uid) = self.rdr.anticoll()
        if error:
            raise Exception("Error in anti collision algorithm")

        global data_position
        sector = data_position["sector_data"]
        block_data = {
            data_position["block_data"]["id"]:id,
            data_position["block_data"]["name"]:name.encode(),
            data_position["block_data"]["surname"]:surname.encode()
        }
        res_data = None
        res_data_tot = []
        for block, data in block_data.items():
            if not self.rdr.card_auth(self.rdr.auth_a, sector*4+block, self.key_a, uid):
                _, res_data = self.rdr.write(sector*4+block, data[:16])
                res_data_tot.append(res_data)

        self.rdr.cleanup()
        self.util.deauth()

        return res_data_tot

def data_to_str(data):
    while 0x00 in data:
        data.remove(0x00)
    return data.decode()
