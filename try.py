try:
    for i in range(3):
        try:
            1/0
        except ZeroDivisionError:
            raise ZeroDivisionError("error : you dived by zero")
        finally:
            print('fianlly executed the following')
            break
except ZeroDivisionError:
    print("outer zeri")