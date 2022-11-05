class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.i = 0

        return self

    def __next__(self):
        self.item_list = self._flatten_list(self.list_of_list)
        if len(self.item_list) == self.i:
            raise StopIteration
        self.item = self.item_list[self.i]
        self.i += 1

        return self.item

    def _flatten_list(self, list_):
        res = []
        for item in list_:
            if isinstance(item, (list, tuple, set)):
                res += self._flatten_list(item)
            else:
                res += [item]

        return res


def test():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print('всё норм')

if __name__ == '__main__':
    test()




