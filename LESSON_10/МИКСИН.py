'''
class Z:
	pass
class H(Z):
        pass

z=Z()
h=H()
print(h.__class__)
'''
class Z:
	pass
class H(Z):
        pass
class P(H, Z):
        pass

z=Z()
h=H()

