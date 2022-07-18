from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

person = Person("Gerald", "witcher", 30, 99)
person2 = Person("Yennefer", "Sorcerrers", 25)
person3 = Person("Yennefer", "Sorcerrers", 25)
print(person)
print(id(person3))
print(id(person2))

print(person>person3)