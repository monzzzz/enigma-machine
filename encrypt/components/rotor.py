class Rotor:
    def __init__(self, wiring, notch, ring_setting=0, initial_position='A'):
        self.wiring = self.create_wiring(wiring)
        self.inverse_wiring = self.create_inverse_wiring(self.wiring)
        self.notch = [ord(n) - ord('A') for n in notch]
        self.ring_setting = ring_setting
        self.position = ord(initial_position.upper()) - ord('A')

    def create_wiring(self, wiring):
        return [ord(c) - ord('A') for c in wiring.upper()]

    def create_inverse_wiring(self, wiring):
        inverse = [0]*26
        for i, c in enumerate(wiring):
            inverse[c] = i
        return inverse

    def forward(self, c):
        offset = (c + self.position - self.ring_setting) % 26
        substituted = self.wiring[offset]
        return (substituted - self.position + self.ring_setting) % 26

    def backward(self, c):
        offset = (c + self.position - self.ring_setting) % 26
        substituted = self.inverse_wiring[offset]
        return (substituted - self.position + self.ring_setting) % 26

    def step(self):
        at_notch = self.position in self.notch
        self.position = (self.position + 1) % 26
        return at_notch
