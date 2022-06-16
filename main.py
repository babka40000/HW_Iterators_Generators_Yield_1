class FlatIterator:
    def __convert_list__(self, list_iter):
        list_res = []
        for list_elem in list_iter:
            for elem in list_elem:
                list_res.append(elem)
        return list_res

    def __init__(self, list_iter):
        self.list_iter = self.__convert_list__(list_iter)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor + 1 == len(self.list_iter):
            raise StopIteration
        self.cursor += 1
        return self.list_iter[self.cursor]


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)
