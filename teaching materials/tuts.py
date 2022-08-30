

# list
names_list = ["kojo", "ama", "kofi"]
b = names_list[1]
a = names_list[-2]
print(a == b)
print(f"these are names of talkative {a}")

#tuple
names_tuple = ("kojo", "ama", "kofi")
print(names_tuple)

# dictionary of names
employee_dict = {
    "employee_1": {
        "name": "kojo",
        "age": 20,
        "gender": "male"
    },
    "employee_2": {
        "name": "kofi",
        "age": 20,
        "gender": "male"
    }
}
print(employee_dict)




# variables and operations
first_name = "john"
number = 2.547
number = round(number)
print(f"{number:.2f}")

last_name = input("Enter last name: ")

print(f"{first_name} {last_name}")


# Functions with additions
def added(a, b):
    c = a + b
    return c

def bodmas(a, b):
    c = a * b + added(a, b)
    return c

print(added(1, 1))
print(added(2, 2))
print(bodmas(2, 2))