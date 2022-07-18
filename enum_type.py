from enum import Enum, auto
from test.test_enum import Fruit
from pickle import dumps, loads

print(Fruit.TOMATO is loads(dumps(Fruit.TOMATO)))

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
class AutoName(Enum):
    def _generate_next_value(self, name, start, count, last_values):
        return self.name

class Color(AutoName):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

print(Color.RED is Color.RED)
print(Color.BLUE is Color.RED)

# print(repr(Color.RED.name))
# print(type(Color))


# class Shake(Enum):
#     VANILLA = 7
#     CHOCOLATE = 4
#     COOKIES = 9
#     MINT = 3

class Mood(Enum):
    """Allowed members and attributes"""
    FUNKY = auto()
    HAPPY = auto()

    def describe(self):
        """describes the enumerated type"""
        return self.name, self.value
    
    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite(cls):
        return cls.HAPPY

print(Mood.favorite())
print(Mood.HAPPY.describe())

# for shake in Shake:
#     print(shake)

# apples = {}
# apples[Color.RED] = 'red delicious'
# apples[Color.GREEN] = 'green also'
# print(apples ==  {Color.GREEN: 'red delicious', Color.GREEN: 'green also'}
# )
# print(apples)

