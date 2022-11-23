type(object)  # <class 'type'>
type(type)  # <class 'type'>
type(int)  # <class 'type'>
type(57)  # <class 'int'>

class MyClass(object): pass
type(MyClass)  # <class 'type'>
type(MyClass())  # <class '__main__.MyClass'>

isinstance(object, object)  # True
isinstance(type, object)  # True
