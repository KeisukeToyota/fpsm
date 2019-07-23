from functools import reduce
from itertools import takewhile, dropwhile, chain


def head(it):
    return next(iter(it))


def tail(it):
    _, *i = it
    return ''.join(i) if type(it) is str else i


def init(it):
    *i, _ = it
    return ''.join(i) if type(it) is str else i


def last(it):
    return next(iter(reversed(it)))


def take(n, it):
    return it[:n] if type(it) is str else list(it)[:n]


def null(it):
    return not list(it)


def foldl(func, it):
    return reduce(func, it, 0)


def foldr(func, it):
    return reduce(lambda x, y: func(y, x), reversed(it), 0)


def concat(it):
    return reduce(lambda x, y: x + y, it)


def concat_map(func, it):
    return concat(map(func, *it))


def product(it):
    return reduce(lambda x, y: x * y, it)


def drop(n, it):
    return list(it)[n:]


def split_at(n, it):
    return [take(n, it), drop(n, it)]


def span(func, it):
    return [list(takewhile(func, it)), list(dropwhile(func, it))]


def elem(n, it):
    return n in list(it)


def not_elem(n, it):
    return n not in list(it)


def flatten(it):
    return chain.from_iterable(it)
