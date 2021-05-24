#!/usr/bin/python3

import time
from pyfingerprint.pyfingerprint import PyFingerprint

#Function to add a new finger in the sensor
def add_finger(f):
    try:
        #Reading the fingerprint
        print('Appoggiare il dito...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)

        #Reading for the second time
        print('Rimuovere il dito...')
        time.sleep(2)
        print('Appoggia lo stesso dito...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x02)

        #COmparing the two fingerprint - if not equal return
        if ( f.compareCharacteristics() == 0 ):
            print('Le impronte non combaciano')
            return
        
        #Adding the fingerprint in the sensor memory
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Impronta aggiunta con successo!')
        print('Posizione impronta: ' + str(positionNumber))

    except Exception as e:
        print('Operazione fallita!')
        print('Exception message: ' + str(e))

#Function to remove finger from the sensor
def remove_finger(f):
    try:
        #Print the list of finger stored
        tableIndex = f.getTemplateIndex(0)
        print('Posizioni occupate:')
        for i in range(0, len(tableIndex)):
            if (tableIndex[i]):
                print(str(i))
        
        #Selecting and delete the finger from the sensor memory
        pos = input('Quale impronta vuoi eliminare? ')
        pos = int(pos)
        f.deleteTemplate(pos)

    except Exception as e:
        print('Operazione fallita!')
        print('Exception message: ' + str(e))

#Function to delete all the finger in the sensor
def clear_finger(f):
    #Cicle to delete all the finger one by one
    tableIndex = f.getTemplateIndex(0)
    for i in range(0, len(tableIndex)):
        if (tableIndex[i]):
            f.deleteTemplate(i)

#Function to print information about the sensor
def info(f):
    try:
        print('Spazi occupati: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    except Exception as e:
        print('Operazione fallita!')
        print('Exception message: ' + str(e))

#Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('Wrong fingerprint password!')

except Exception as e:
    print('Error during fingerprint initialization!')
    print('Exception message: ' + str(e))
    exit(1)

while True:
    #Printing the menu
    print('What will you do?')
    print('0) Exit')
    print('1) Info')
    print('2) Add finger')
    print('3) Remove finger')
    print('4) Clear finger memory')
    
    #Select and execute the choose
    choose = input('Inserire scelta...\n')
    choose = int(choose)

    if (choose == 0):
        exit(0)
    elif (choose == 1):
        info(f)
    elif (choose == 2):
        add_finger(f)
    elif (choose == 3):
        remove_finger(f)
    elif (choose == 4):
        clear_finger(f)