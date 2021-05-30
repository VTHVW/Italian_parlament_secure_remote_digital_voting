#!/usr/bin/python3

import os
from pyfingerprint.pyfingerprint import PyFingerprint

#Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('Wrong fingerprint password!')

except Exception as e:
    print('Error during fingerprint initialization!')
    print('Exception message: ' + str(e))
    exit(1)

#Find rows and colums number (for a nicest print...)
rows, columns = os.popen('stty size', 'r').read().split()

while(True):
    try:
        #Wait for the finger
        state = 1
        while ( f.readImage() == False ):
            #Print a str in the centre of display
            if (state != 0):
                state = 0
                os.system('clear')

                cont = 0
                while cont < (int(rows)/2):
                    print()
                    cont = cont + 1
                cont = 0
                while cont < ((int(columns)/2) - 16):
                    print(' ', end = '')
                    cont = cont + 1
                
                print("Appoggiare il dito sul sensore...")
            pass

        #Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        #Searchs template
        result = f.searchTemplate()
        if (result[0] == -1 ):
            #Print a str in the centre of display
            if (state != 1):
                state = 1
                os.system('clear')

                cont = 0
                while cont < (int(rows)/2):
                    print()
                    cont = cont + 1
                cont = 0
                while cont < ((int(columns)/2) - 10):
                    print(' ', end = '')
                    cont = cont + 1

                print('Impronta non trovata')
            pass
        else:
            os.system('clear')

            #Another centred print
            cont = 0
            while cont < (int(rows)/2):
                print()
                cont = cont + 1
            cont = 0
            while cont < ((int(columns)/2) - 13):
                print(' ', end = '')
                cont = cont + 1

            print("Impronta trovata, login...")

            #Login
            os.system('login -f -p pi')
            #os.system('startx')
            #os.system('systemctl start lightdm')
            os.system('clear')
            exit(0)
    
    except Exception as e:
        print('Errore: ')
        print('Exception message: ' + str(e))
        exit(1)