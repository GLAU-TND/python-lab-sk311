try:
    x = 10
    y = int("bharat")
    z = x + y
    print(z)
except ValueError as e:
    print(e)
try:
    x = 10
    y = "bharat"
    z = x + y
    print(z)
except TypeError as e:
    print(e)

try:
    x = 10
    print(x.count)
except AttributeError as e:
    print(e)
