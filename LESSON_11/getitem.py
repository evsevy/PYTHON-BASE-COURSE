
class DATA():
    
    def __init__(self, directory, file):
        self.directory = directory
        self.files = list(file)

        def __getitem__(self, item):
            return self.marks[item]
        """
        def __setitem__(self, key, value):
            self.files[key] = value
"""
d = DATA("python", [1,2,3,4,5,6,7,8,9])
#d[3] = 10

#print(d.files[3])
#print(d[3])
print(d.files)


