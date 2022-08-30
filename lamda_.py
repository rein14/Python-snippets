# x = lambda a : a + 10

# print(x(5))

# x = lambda a , b, c : a + b + c
# print(x(5, 6, 2))


my_list = [1,5,6,7,8,9,0,23,22]

new_list = list(filter(lambda x: (x%2 == 0), my_list))
another_list = list(map(lambda x: x * 2, my_list))

print(new_list)
print(another_list)


def calc(new):
    x = 2
    def calc2():
        nonlocal x 
        x = 5
        print("inner:",x, new)
    
    calc2()

calc(5)