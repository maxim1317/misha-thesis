def pretty_time_delta(seconds):
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    # print(days)
    if days > 0:
        return '%d days, %d hours, %d minutes' % (days, hours, minutes)
    elif hours > 0:
        return '%d hours, %d minutes' % (hours, minutes)
    else:
        return '%d minutes' % minutes


def read_yaml(path):
    '''Reads JSON file and returns a dict
    '''
    import yaml

    with open(path, 'r') as raw:
        s = raw.read()

        data = yaml.load(s)
    return data


def write_yaml(data, path):
    '''Writes dict as JSON to file
    '''
    from json import dump

    with open(path, 'w') as raw:
        dump(data, raw, indent=4)
    return


def _test_pretty_time_delta():
    print(pretty_time_delta(60000000))


def _test_read_yaml():
    print(read_yaml('../conf/simulation.yml'))


if __name__ == '__main__':
    _test_pretty_time_delta()
    _test_read_yaml()
