#!/usr/bin/python3

import time
import os
from pyfingerprint.pyfingerprint import PyFingerprint

def add_finger(f):
    try:
        print("Appoggiare il dito...")
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)

        print("Rimuovere il dito...")
        time.sleep(2)
        print("Appoggia lo stesso dito...")
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x02)

        if ( f.compareCharacteristics() == 0 ):
            print("Le impronte non combaciano")
            return
        
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print("Impronta aggiunta con successo!")
        print("Posizione impronta: " + str(positionNumber))

    except Exception as e:
        print("Operazione fallita!")
        print('Exception message: ' + str(e))

def remove_finger(f):
    try:
        tableIndex = f.getTemplateIndex(0)

        print("Posizioni occupate:")
        for i in range(0, len(tableIndex)):
            if (tableIndex[i]):
                print(str(i))
        
        pos = input("Quale impronta vuoi eliminare? ")
        pos = int(pos)

        f.deleteTemplate(pos)

    except Exception as e:
        print("Operazione fallita!")
        print('Exception message: ' + str(e))

def clear_finger(f):
    tableIndex = f.getTemplateIndex(0)
    for i in range(0, len(tableIndex)):
        if (tableIndex[i]):
            f.deleteTemplate(i)

def info(f):
    try:
        print('Spazi occupati: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    except Exception as e:
        print("Operazione fallita!")
        print('Exception message: ' + str(e))

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('Wrong fingerprint password!')

except Exception as e:
    print('Error during fingerprint initialization!')
    print('Exception message: ' + str(e))
    exit(1)

while True:
    print("What will you do?")
    print("0) Exit")
    print("1) Info")
    print("2) Add finger")
    print("3) Remove finger")
    print("4) Clear finger memory")
    

    chose = input("Inserire scelta...\n")
    chose = int(chose)

    if (chose == 0):
        exit(0)
    elif (chose == 1):
        info(f)
    elif (chose == 2):
        add_finger(f)
    elif (chose == 3):
        remove_finger(f)
    elif (chose == 4):
        clear_finger(f)