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
    valid_response = http_response(input('Please enter a valid response: 400-500>>>'))
    match status:
        case 400:
            return 'Bad request'
        case 500:
            return 'Internal Server Error'
        case 403:
            return 'Forbidden'
        case 404:
            return 'Not Found'
    return valid_response


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def where_is_point(self, point):
        match point:
            case Point(x=0, y=0):
                print('Origin')
            case Point(x=0, y=y):
                print(f'Y={y}')
            case Point(x=x, y=0):
                print(f'X={x}')
            case Point():
                print('Something else...')
            case _:
                print('Not a point')
