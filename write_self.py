# import sys

# if(i := input())[0] == "q" or i == "exit":
#     sys.exit()

# l = [1,2,4,5,6,7,8,9]

# head, *tail = l[0], l[1:]

# print(tail)


#unpacking
# def verify_check_digits(digits):
#     *digits, check_digit = digits
#     weight = 2
#     acc = 0
#     for digit in reversed(digits):
#         value = digit * weight
#         acc += (value // 10) + (value % 10)
#         weight = 3 - weight   
#     return (9 * acc % 10) == check_digit

# print(verify_check_digits([7, 9, 9, 2, 7, 3, 9, 8, 7, 1, 3]))


#zip
# firsts = ["ama","kojo"]
# second = ["smith", "Doe"]
# print(dict(zip(firsts, second)))

# for first, second in zip(firsts, second):
#     print(f"{first} {second}")

# d = {"a": 1, "b": 2, "c": 3}
# key = "a"

# print(d.get(key,None))


#eafp vs lbl
# import pathlib
# print("what file should i read")

# filepath = input(" >> ")
# if pathlib.Path(filepath).exists():
#     with open(filepath, 'r') as f:
#         contents = f.read()
#         print(contents)
# else:
#     print("file doesnt exist")

# try:
#     with open(filepath, 'r') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print("file does not exist")
# else:
#     pass

# from pathlib import PurePath
# print(PurePath('a/b/c.py').match('a/*.py'))


#csv writer
# import csv
# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name':'kwame', 'last_name':'Opoku'})


#Enumerate
# weekdays = ["Monday", "Tuesday", "Wednesday",]
# for i, day in enumerate(weekdays, 32):
#     print(f"{i}: {day}")

# pages = [5, 17, 31, 50] 
# print(dict(zip(pages, pages[1:])))
# for i, (start,end) in enumerate(zip(pages, pages[1:]), start=1):
#     print(f"{i}: {end-start} pages long")


#__repr__ and __str__
# import datetime 
# date = datetime.datetime(2021,2,2)
# print(repr(date))
# print(str(date))

#structural pattern matching
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# def factorial(n):
#     match n:
#         case 0 | 1:
#             return 1
#         case _:
#             return n * factorial(n-1)
# print(factorial(5))



# class Point2D:

#     __match_args__ = ("x", "y")
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def describe_point(point):
#     match point:
#         case Point2D(0,0):
#             desc = "at the origin"
#         case Point2D(x, 0):
#             desc = f"in the horizontal axis, at x = {x}"
#         case Point2D(x, y):
#             desc = f"f at {point}"
#     return "the point is " + desc

# # Prints "The point is at the origin"
# print(describe_point(Point2D(1, 0))
# import ast

# def prefix(tree):
#     match tree:
#         case ast.Expression(expr):
#             return prefix(expr)
#         case ast.Constant(value=v):
#             return str(v)
#         case ast.BinOp(lhs, op, rhs):
#             match op:
#                 case ast.Add():
#                     sop = "+"
#                 case ast.Sub():
#                     sop = "-"
#                 case ast.Mult():
#                     sop = "*"
#                 case ast.Div():
#                     sop = "/"
#                 case _:
#                     raise NotImplementedError()
#             return f"{sop} {prefix(lhs)} {prefix(rhs)}"
#         case _:
#             raise NotImplementedError()


# print(prefix(ast.parse("1 + 2 + 3", mode="eval")))

# def pretty_pprint(arg):
#     if isinstance(arg, complex):
#         print(f"{arg.real} + {arg.imag}i")
#     elif isinstance(arg, (list, tuple)):
#         for i, elem in enumerate(arg):
#             print(i, elem)
#     elif isinstance(arg, dict):
#         for key, value in arg.items():
#             print(f"{key}: {value}")
#     else:
#         print(arg)


import functools
 

@functools.singledispatch
def pretty_pprint(arg):
    print(arg)

@pretty_pprint.register(complex)
def _(arg):
    print(f"{arg.real} + {arg.imag}i")

@pretty_pprint.register(list)
@pretty_pprint.register(tuple)
def _(arg):
    for i, elem in enumerate(arg):
        print(i, elem)

@pretty_pprint.register(dict)
def _(arg):
    for key, value in arg.items():
        print(f"{key}: {value}")

print(pretty_pprint(8))
