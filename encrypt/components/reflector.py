class Reflector:
    def __init__(self, wiring):
        self.wiring = self.create_wiring(wiring)

    def create_wiring(self, wiring):
        return [ord(c) - ord('A') for c in wiring.upper()]

    def reflect(self, c):
        return self.wiring[c]
