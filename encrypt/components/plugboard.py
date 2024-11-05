import string

class Plugboard:
    def __init__(self, wiring=''):
        self.wiring = self.create_wiring(wiring)
        
    def create_wiring(self, wiring):
        alphabet = list(string.ascii_uppercase)
        wiring_dict = {letter: letter for letter in alphabet}
        pairs = wiring.upper().split()
        for pair in pairs:
            if len(pair) == 2:
                a, b = pair[0], pair[1]
                wiring_dict[a], wiring_dict[b] = b, a
        return wiring_dict

    def swap(self, c):
        return self.wiring.get(c, c)

