class Queue(object):
    def __init__(self, params):
        self.q = []

    def push(self, ship):
        self.q.append(ship)

    def pop(self):
        if len(self.q) > 0:
            return (True, self.q.pop(0))
        return (False, None)

    def sort(self, storehouse):
        pass
