import numbers
import string
import timeit 
from dataclasses import dataclass
from functools import partial

@dataclass(slots=False)
class Person:
    name :str
    address : str
    email :str

@dataclass(slots=True)
class PersonSlots:
    name : str
    address : str
    email : str

@dataclass(slots=True)
class EmployeeSlots:
    dept: str

"""class PersonEmployee(PersonSlots, EmployeeSlots):
    pass
"""

def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main Street"
    person.address
    del person.address

def main(): 
    person = Person("John", "123 Main Street", "john@example.com")
    person_slots = PersonSlots("John", "123 Main Street", "John@example.com")
    no_slots = min(timeit.repeat(partial(get_set_delete, person), number = 1000000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number = 1000000))
    print(f"No slots: {no_slots}")
    print(f"WIth slots: {slots}")
    print(f"Total slots: {(no_slots - slots)/ no_slots:.2%}")

if __name__ == "__main__":
    main()