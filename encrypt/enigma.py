from components.plugboard import Plugboard

class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard_settings=''):
        self.plugboard = Plugboard(plugboard_settings)
        self.rotors = rotors
        self.reflector = reflector

    def encode_char(self, c):
        if not c.isalpha():
            return c
        c = c.upper()
        c = ord(self.plugboard.swap(c)) - ord('A')
        
        rotation = True
        for i in range(len(self.rotors)):
            if rotation:
                rotation = self.rotors[i].step()
            else:
                break

        for rotor in reversed(self.rotors):
            c = rotor.forward(c)

        c = self.reflector.reflect(c)

        for rotor in self.rotors:
            c = rotor.backward(c)

        c = self.plugboard.swap(chr(c + ord('A')))
        return c

    def encrypt(self, text):
        return ''.join(self.encode_char(c) for c in text)
    