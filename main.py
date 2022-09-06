nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, [9,[8,7,[6,[5,[4],3],2],1],0]],
]


class FlatIterator:
    def __init__(self, nested_list):
        self.flat_list = []
        self.unpack_list(nested_list)
    def __iter__(self):
        return self
    def __next__(self):
        if not self.flat_list:
            raise StopIteration
        item = self.flat_list.pop(0)
        return item
    def unpack_list(self, l):
        for i in l:
            if isinstance(i, list):
                self.unpack_list(i)
            else:
                self.flat_list.append(i)

for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print('flat_list iterator =', flat_list)

print('______'*20)


_flat_l = []
def unpack_list(l):
    for i in l:
        if isinstance(i, list):
            unpack_list(i)
        else:
            _flat_l.append(i)
def flat_generator(nested_list):
    unpack_list(nested_list)
    while _flat_l:
        yield _flat_l.pop(0)

for item in flat_generator(nested_list):
    print(item)
flat_list = [item for item in flat_generator(nested_list)]
print('flat_list generator =', flat_list)