"""
class Calendar:
    __slots__ = ('D', 'M', 'Y')

    def __init__(self, d = 0, m = 0, y = 0):
        self.D = d
        self.M = m
        self.Y = y
        print(self)

    def __setattr__(self, key, value):
        if isinstance(value, int):
            print('ГОТОВО')
        else:
            raise AttributeError

    def __getattr__(self, item):
        print('ГОТОВО2')


c = Calendar(1, 12, 2004)
"""
class Data:
    pass
d = Data()
d.id = 10
print(d.id)
# АНАЛОГб если имя атрибута не статично:
setattr(d, 'id', 20)
print(d.id)

##########################################
d = Data()
attr_name = input('Enter the attribute name:\n')
attr_value = input('Enter the attribute value:\n')
setattr(d, attr_name, attr_value)
print('Data attribute =', attr_name, 'and its value =', getattr(d, attr_name))


