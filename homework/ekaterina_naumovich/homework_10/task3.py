def operation(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')
        elif first < 0 and second < 0:
            return func(first, second, '*')
        else:
            print('error')
            return None
    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        print('wrong operation')
        return None

result = calc(int(input('first number: ')), int(input('second number: ')))
print(f'your result is: {result}')
