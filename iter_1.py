class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.i = 0
        self.j = -1
        return self

    def __next__(self):
        if self.j < len(self.list_of_list[self.i]) - 1:
            self.j += 1
        else:
            self.j = 0
            self.i += 1
        if self.i >= len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.i][self.j]

        return item


def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print('всё норм')


if __name__ == '__main__':
    test()
