
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


