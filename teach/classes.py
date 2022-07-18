# class Complex:
#     def __init__(self, realpart, imagpart, new_name):
#         self.r = realpart
#         self.i = imagpart
#         self.n = new_name

# x = Complex(3.0, -5, 20)
# print(x.r, x.i, x.n)


# x.counter = 2
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)

class Dog:

    all_tricks = []

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        for new_trick in trick
        if trick not in self.all_tricks:
            self.all_tricks.append(trick)


d = Dog('Rocky', 'canine')
g = Dog('Esther', 'Rotweiler')
d.add_trick(['roll over', 'bite'])
g.add_trick('play dead')
# print(d.tricks)

x = Dog.all_tricks
print(x)
