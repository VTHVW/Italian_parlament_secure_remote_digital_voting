from gpiozero import Button

class voting_buttons():

    def __init__(self, button_yes='GPIO26', button_no='GPIO19', button_abstained='GPIO13'):
        self.value = {'press': 0, 'button': 'none'}
        self.voted = True

        self.button_yes = Button(button_yes)
        self.button_no = Button(button_no)
        self.button_abstained = Button(button_abstained)

        self.button_no.when_pressed = self.button_no_pressed
        self.button_yes.when_pressed = self.button_yes_pressed
        self.button_abstained.when_pressed = self.button_abstained_pressed

    def button_no_pressed(self):
        if not self.voted:
            if self.value['button'] == 'no':
                self.value['press'] = 2
                self.voted = True
            else:
                self.value['button'] = 'no'
                self.value['press'] = 1

    def button_yes_pressed(self):
        if not self.voted:
            if self.value['button'] == 'yes':
                self.value['press'] = 2
                self.voted = True
            else:
                self.value['button'] = 'yes'
                self.value['press'] = 1

    def button_abstained_pressed(self):
        if not self.voted:
            if self.value['button'] == 'abstained':
                self.value['press'] = 2
                self.voted = True
            else:
                self.value['button'] = 'abstained'
                self.value['press'] = 1

    def new_voting_session(self):
        self.voted = False
        self.value = {'press': 0, 'button': None}
