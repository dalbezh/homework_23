from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def unique_query(data, *args, **kwargs):
    return set(data)


def limit_query(value: str, data):
    limit = int(value)
    return list(data)[:limit]


def map_query(value: str, data):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data):
    if value == 'desk':
        return sorted(data, reverse=True)
    else:
        return sorted(data)


command = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query
}


def read_file(file):
    with open(file, "r", encoding='utf-8') as f:
        for line in f:
            yield line


def build_query(cmd, value, file, data):
    if data is None:
        preparing_data = read_file(file)
    else:
        preparing_data = data
    return list(command[cmd](value=value, data=preparing_data))
