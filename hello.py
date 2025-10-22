print(23+34)

def func(a, b):
    c = a+b
    if(a+b>5):
        return func(1, 2) +40
    else:
        return c
    # return c

k = func(3, 4)
print(k)