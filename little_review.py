import collections
from enum import Enum

a = ['Mary', 'had', 'a', 'little', 'lamb']

for word in enumerate(a):
    print(word)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} is not a prime number!')
            break
    else:
        print(f"{n} is a prime number!")


def http_response(status):
    match status:
        case 400:
            return 'Bad request'
        case 500:
            return 'Internal Server Error'
        case 403:
            return 'Forbidden'
        case 404:
            return 'Not Found'

    # class Point:
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y


#
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'
# color = Color(input('Choose a color: "red" or "green" or "blue"'))
#
# match color:
#     case Color.RED:
#         print("I'm feeling a little RED")
#     case Color.GREEN:
#         print("I'm feeling a little GREEN")
#     case Color.BLUE:
#         print("I'm feeling a little BLUE")

def fibonacci(n):
    print("Fibonacci")
    result = []
    a, b = 0, 1
    while a < n:
        # print(a, end=" ")
        result.append(a)
        a, b = b, a + b
    return result


fib = fibonacci(100)
print(fib)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('do you want to quit?')
def fill(a, l=[]):
    if l is None:
        l = []
    l.append(a)
    return l, len(l)


fi = fill(1)
print(fi)
f1 = fill(2)
print(f1)
f2 = fill(3)
print(f2)
f3 = fill(4)
print(f3)

b = {'fname': 'Mike', 'lname': 'Pence', 'Job': 'Former SG White House'}
for key, value in b.items():
    print(f"{key}: {value}")


def mixed(arg, /, standard, *, kword):
    """A function that returns and only_position and an only_keyword arguments"""
    print(f"{arg}, {standard}, {kword}")


mixed(1, 2, kword=5)


def info(*name, sep='.'):
    return sep.join(name)


print(info('ibrahim01@gmail', 'com'))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda x: x[0])

print('Mixed Docs:', mixed.__doc__)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
var = [[row[i] for row in matrix] for i in range(4)]
print(var)
# for i in range(4):
#     print(matrix[i])

a = 'abracadabra'
value = {x for x in a if x not in 'ab'}
print(value)

val = {'name': 'IB', 'lastName': 'Zakari'}
for i in val.get('name'):
    # print(i, end='')
    pass

for key, value in val.items():
    # print(key, value, end=' ')
    pass

# print(val.popitem())

val.update({'name': 'Tanko'})
print(val)

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(s)
s *= 2
print(s)
z = 'ibrahim'
print(z.capitalize())
print(z.endswith('m'))
vt = bytearray(b'mhdAfroTrap')
print(vt)

uv = {'ali', 'manzo'}
tv = {'bound', 'target'}

print(uv.intersection() | tv.intersection())
uv.add('zero')
print(uv.intersection() | tv.intersection())
print(b.copy())
print(list(reversed(b)))
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

n = 0
for val in values:
    n += val
print(n)


def average(val: list[float]) -> float:
    """

    :type val: object
    """
    return sum(val) / len(val)

cb = average([12, 13, 14, 15, 16, 17])
print(cb)

bn = list[float]
print(type(bn))


class MyClass:
    x = 5

print(MyClass.x)