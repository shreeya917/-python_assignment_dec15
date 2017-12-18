# Q5. Code a Function that simply returns ("Hello", 45, 23.3)and call this function and unpack the returned values and print it.

def f():
    return ("Hello", 45, 23.3)


x, y, z = f()
print(x)
print(y)
print(z)


def unpack():
    return ('Hello',123,235)

x,y,z=unpack()