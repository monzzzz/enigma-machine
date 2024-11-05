import string
from enigma import EnigmaMachine
from components.rotor import Rotor
from components.reflector import Reflector
if __name__ == "__main__":
    rotors = [
        Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
        Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
        Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
    ]
    reflector = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    machine = EnigmaMachine(rotors, reflector, 'AV BS CG DL FU HZ IN KM OW RX')
    text = 'HELLO WORLD'
    encrypted = machine.encrypt(text)
    print(encrypted)