def abc(a, b):
    c = a + b
    if c < 150:
        raise TypeError("Custom Exception Occurred")
    else:
       return c
class MyException(Exception):
    def __init__(self,c):
        self.c = c
        def __str__(self):
            return self.c

a = int(input("Enter the number"))
b = int(input("Enter the number"))
print(abc(a, b))
