class Movement:
    def __init__(self, params):
        self.ships = {}

    def add(self, ship):
        self.ships[ship] = 1  # хитрая формула

    def tick(self):
        for k, v in self.ships.items():
            if self.ships[k] > 0:
                self.ships[k] -= 1

    def ready(self):
        to_ready = []
        for k, v in self.ships.items():
            if v == 0:
                to_ready.append(k)
        for a in to_ready:
            self.ships.pop(a)
        return to_ready

    def __len__(self):
        return len(self.ships)
