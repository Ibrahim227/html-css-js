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
