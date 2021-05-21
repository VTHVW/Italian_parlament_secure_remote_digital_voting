from gpiozero import Button

class voting_buttons():

    def __init__(self, button_yes = "GPIO26", button_no = "GPIO19", button_abstained = "GPIO13"):        
        self.value = {'press': 0, 'button': 'none'}
        self.temp = "none"
        sel.cont = 0
        
        self.button_yes = Button(button_yes)
        self.button_no = Button(button_no)
        self.button_abstained = Button(button_abstained)

        self.button_no.when_pressed = self.button_no_pressed
        self.button_yes.when_pressed = self.button_yes_pressed
        self.button_abstained.when_pressed = self.button_absteined_pressed

    def button_no_pressed(self):
        self.value['button'] = 'non favorevole'
        
        if(temp == value['button']):
            value['press'] += 1
            if(value['press'] == 2):
                print('voto non favorevole confermato')
        elif (temp != value['button']):
            if(value['press'] == 2):
               print('preferenza già confermata')
            else:
                value['press'] = 1
                print('non favorevole')
        temp = value['button']
        
        
    def button_yes_pressed(self):
        self.value['button'] = 'favorevole'
        
        if(temp == self.value['button']):
            self.value['press'] += 1
            if(self.value['press'] == 2):
                print('voto favorevole confermato')
        elif (self.temp != self.value['button']):
            if(self.value['press'] == 2):
               print('preferenza già confermata')
            else:
                self.value['press'] = 1
                print('favorevole')
        self.temp = self.value['button']
        
    def button_absteined_pressed(self):
        self.value['button'] = 'absteined'
        if(self.temp == self.value['button']):
            self.value['press'] += 1
            if(self.value['press'] == 2):
                print('astensione confermata')
        elif (self.temp != self.value['button']):
            if(self.value['press'] == 2):
                print('preferenza già confermata')
            else:
                self.value['press'] = 1
                print('astensione')
        self.temp = self.value['button']
