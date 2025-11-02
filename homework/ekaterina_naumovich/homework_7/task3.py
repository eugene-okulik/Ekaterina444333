result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'


def results(*args):
    for arg in args:
        num = int(arg.split(':')[1])
        print(num + 10)


results(result1, result2, result3)
