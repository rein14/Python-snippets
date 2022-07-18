from datetime import datetime
from typing import Callable
from functools import partial

GreetingReader = Callable[[], str]
GreetingFunction = Callable[[str], str]

def greet(name: str, greeting_reader: GreetingReader) -> str:
    """return greeting"""
    if name == "richy":
        return "burger off"
    return f"{name} {greeting_reader()}"

def greet_list(names: list[str], greeting_fn: GreetingFunction) -> list[str]:
    """return a list of greeting"""
    return [greeting_fn(name) for name in names]

def read_greeting() -> str:
    """read greeting"""
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good moring"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def read_name() -> str:
    """return name input"""
    return input("Enter your name: ")


def main() -> None:
    """main function"""
    greet_fn = partial(greet, greeting_reader=read_greeting)
    print(greet_fn(read_name()))
    print(greet_list(["John", "Jane", "Joe"], greet_fn))

if  __name__ == "__main__":
    main()
