import types
from collections.abc import Iterable

def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for i in flat_generator(item):
                yield i
        else:
            yield item


def test():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    print('всё норм')


if __name__ == '__main__':
    test()
