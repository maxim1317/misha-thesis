class Storehouse(object):
    def __init__(self, params):
        self.cargo = {0: 1, 1: 1, 2: 2}
        self.max_cargo = {0: 10, 1: 10, 2: 20}

    def load(self, ship_cargo):
        for k, v in ship_cargo.items():
            if self.max_cargo[k] <= (self.cargo[k] + v):
                self.cargo[k] = self.max_cargo[k]
            else:
                self.cargo[k] += v

    def tick(self):
        for k, v in self.cargo.items():
            if self.cargo[k] == self.max_cargo[k]:
                print('Cargo', k, 'maxed out')
