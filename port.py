import random


class Ship(object):
    def __init__(self):
        self.cargo = {
            0: 1,
            1: 1,
            2: 2
        }
        self.size = random.randint(0, 10)

        # stats
        self.time_in_queue = 0
        self.time_in_movement = 0
        self.time_in_unloading = 0


class Queue(object):
    def __init__(self):
        self.q = []

    def push(self, ship):
        self.q.append(ship)

    def pop(self):
        if len(self.q) > 0:
            return (True, self.q.pop(0))
        return (False, None)

    def sort(self, storehouse):
        pass


class Movement:
    def __init__(self):
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


class Unloading:
    def __init__(self, speed):
        self.speed = speed
        self.ship = None
        self.time_left = 0

    def load(self, ship):
        self.ship = ship
        self.time_left = int(ship.size / self.speed)  # хитрая формула

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1

    def ready(self):
        if self.time_left == 0:
            ship = self.ship
            self.ship = None
            return ship
        return None

    def free(self):
        if self.ship is None:
            return True
        return False


class Port(object):
    def __init__(self):
        self.unloadings = [Unloading(2)] * 3

    def free(self):
        free_u = []
        for u in range(len(self.unloadings)):
            if self.unloadings[u].free():
                free_u.append(u)
        return free_u

    def load(self, ship):
        for a in self.unloadings:
            if a.free():
                a.load(ship)
                return True
        return False

    def tick(self):
        for un in self.unloadings:
            un.tick()


class Storehouse:
    def __init__(self):
        self.cargo = {0: 1, 1: 1, 2: 2}
        self.max_cargo = {0: 10, 1: 10, 2: 20}

    def load(self, ship_cargo):
        for k, v in ship_cargo.items():
            if self.max_cargo[k] <= (self.cargo[k] + v):
                self.cargo[k] = self.max_cargo[k]
            else:
                self.cargo[k] += v


class Generator(object):
    def __init__(self):
        pass

    def next(self):
        from random import triangular
        ships = []
        ship_num = int(triangular(0, 3, 0))

        for i in range(ship_num):
            ships.append(Ship())

        return ships


class Manager(object):
    def __init__(self):
        self.time = 0
        self.generator = Generator()
        self.queue = Queue()
        self.movement = Movement()
        self.port = Port()
        self.storehouse = Storehouse()

        self.generated_total = 0
        self.can_move_ticks = 0

    def tick(self):
        self.port.tick()
        self.movement.tick()

        ships = self.generator.next()
        self.generated_total += len(ships)

        for ship in ships:
            self.queue.push(ship)

        self.queue.sort(self.storehouse)
        if self.can_move():
            y, ship_to_process = self.queue.pop()
            if y:
                self.movement.add(ship_to_process)
            for ship in self.movement.ready():
                # print('load to port')
                self.port.load(ship)

        self.can_move_ticks += int(self.can_move())

        for un in self.port.unloadings:
            sh = un.ready()
            if sh is not None:
                self.storehouse.load(sh.cargo)

    def can_move(self):
        if len(self.movement) < len(self.port.free()):
            return True
        else:
            return False


def main():
    manager = Manager()
    s = 0
    while True and s <= 100:
        manager.tick()
        # print manager stats
        s += 1
    print(manager.storehouse.cargo)
    print(manager.generated_total)
    print(manager.can_move_ticks)


if __name__ == '__main__':
    main()
