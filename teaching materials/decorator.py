def percent(func):
    def inner(*args, **kwargs):
        print("#" * 40)
        func(*args, **kwargs)
        print("#" * 40)
    return inner
    
def percent2(func):
    def inner(*args, **kwargs):
        print("$" * 40)
        func(*args, **kwargs)
        print("$" * 40)
    return inner

@percent2
@percent
def printer(msg):
    print(msg)

printer("Hello")