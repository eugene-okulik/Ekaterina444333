def repeat_me(func):
    def wrapper(text, count):
        for i in range(count):
            func(text)
    return wrapper


@repeat_me
def example(text):
    print(text)

example('print me', count = 2)


def repeat_me2(count):
    def decorator(func):
        def wrapper(text):
            for i in range(count):
                func(text)
        return wrapper
    return decorator


@repeat_me2(count=2)
def example(text):
    print(text)


example('print me')
