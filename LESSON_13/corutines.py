

def coroutine(f):
    def wrap(*args,**kwargs):
        gen = f(*args,**kwargs)
        gen.send(None)
        return gen
    return wrap
 
@coroutine
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print (history)
            continue
        result = x + y
        print (result)
        history.append(result)
c = calc()
print(c.send((1,2)))
print(c.send(('h',0)))


# Python3 program for demonstrating
# coroutine execution

def print_name(prefix):
	print("Searching prefix:{}".format(prefix))
	while True:
		name = (yield)
		if prefix in name:
			print(name)

# calling coroutine, nothing will happen
corou = print_name("Dear")

# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()

# sending inputs
corou.send("Evgen")
corou.send("Dear Evgen")

