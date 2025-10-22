print(23+34)

def func(a, b):
    c = a+b
    if(a+b>5):
        func(func(5, func(4, 7)), func(5, 7))
    else:
        func(func(4, 96), 7)
    return c

k = func(3, 4)
print(k)