from src import Manager


def run():
    manager = Manager('conf/simulation.yml')
    manager.run()


if __name__ == '__main__':
    run()
