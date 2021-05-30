#!/usr/bin/python3 

from pathlib import Path
import time
import os
import hashlib

class Votazioni():

    #Count the number of ID
    def count_id():
        try:
            file = open('elenco.txt', 'r')
            count = int(file.read().count('\n'))
            file.close
            return count

        except Exception as e:
            print('Error!')
            print('Exception message: ' + str(e))
            return e

    #Constructor
    def __init__(self):
        self.defid = self.count_id()
    
    #Set the id of the vote to use
    def set_id(self, id):
        self.defid = int(id)
    
    #Create a new vote
    def create_vote(self, name, desc, type, who):
        try:
            #Save current date and time
            datetime = time.strftime('%d/%m/%Y-%H:%M:%S')
            
            #Update the ID
            fileid = self.count_id + 1
            self.defid = fileid
            
            #Add the vote to the vote list file
            file = open('elenco.txt', 'a')
            file.write(str(fileid) + '_' + name + '_' + datetime + '\n')
            file.close()

            #Create the vote file and write things
            file = open(str(fileid) + '.txt', 'w')
            file.write('0\n')
            file.write(datetime + '\n')
            file.write(name + '\n')
            file.write(desc + '\n')
            file.write(type + '\n')
            file.write(who + '\n')
            file.close()

            return fileid

        except Exception as e:
            print('Error!')
            print('Exception message: ' + str(e))
            return e
    
    #Add a vote to current vote
    def add_vote(self,):
        file = open(str(self.id) + '.txt', 'a')

    #Close current vote
    def close_vote(self):
        try:
            filename = str(self.defid) + '.txt'
            file = open(filename, 'r+')
            file.write('0')
            file.close()
            os.system('chmod 444' + filename)
            
            return 0
        
        except Exception as e:
            print('Error!')
            print('Exception message: ' + str(e))
            return e
    
    #Close vote
    def close_vote(self, id):
        try:
            filename = str(id) + '.txt'
            file = open(filename, 'r+')
            file.write('0')
            file.close()
            os.system('chmod 444' + filename)
            
            return 0
        
        except Exception as e:
            print('Error!')
            print('Exception message: ' + str(e))
            return e
    
    #Return a dictionary with the result of the default vote
    def res_vote(self):
        try:
            #Open file and verify that the vote is closed
            file = open(str(id) + '.txt', 'r')
            if (int(file.readline()) == 0):
                print('Votazione ancora in corso')
                return 1

            #Read and save basic information
            datetime = file.readline()
            name = file.readline()
            desc = file.readline()
            type = file.readline()
            who = file.readline()

            #Initialize counter
            count0 = 0
            count1 = 0
            count2 = 0

            #Read and count the vote
            text = file.readline()
            while (text != ''):
                if (int(text[0]) == 0):
                    count0 = count0 + 1
                elif (int(text[0]) == 1):
                    count1 = count1 + 1
                elif (int(text[0]) == 2):
                    count2 = count2 + 1
            
            #Generate the hash from the file
            file.seek(0, 0)
            md5 = hashlib.md5(file.read())
            hash = md5.hexdigest()

            file.close()

        except Exception as e:
            print('Error!')
            print('Exception message: ' + str(e))
            return e