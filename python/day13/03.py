def my_decorator(fun):

    def wrapper(*args, **kwargs): # for func with arguments 
        print('Function execution started')

        fun(*args, **kwargs)

        print('Execution is completed')

    return wrapper


@my_decorator
def add(a, b):
    print(a + b)


add(12, 34)