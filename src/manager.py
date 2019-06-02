class Manager(object):
    def __init__(self, config_path):
        from . import blocks

        self.config = self.get_confif(config_path)

        self.time = 0
        self.generator = blocks.Generator(self.config["generator"])
        self.queue = blocks.Queue(self.config["queue"])
        self.movement = blocks.Movement(self.config["movement"])
        self.port = blocks.Port(self.config["port"])
        self.storehouse = blocks.Storehouse(self.config["storehouse"])

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
                self.storehouse.tick()

        self.print_stats()

        self.time += 1

    def run(self, sim_time=100):

        ticks = 0
        while ticks <= sim_time:
            self.tick()
            # print manager stats
            ticks += 1

        return ticks

    def print_stats(self):
        from .utils import pretty_time_delta
        time = pretty_time_delta(self.time * 60)
        print("Time passed:", time)
        return

    def can_move(self):
        if len(self.movement) < len(self.port.free()):
            return True
        else:
            return False

    def get_confif(self, path):
        from .utils import read_yaml

        conf = read_yaml(path)
        return conf
