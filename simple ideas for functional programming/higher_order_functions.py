from datetime import datetime
 
def greet(name: str, greeting_intro: str) -> str:
    """return greeting"""
    return f"{name} {greeting_intro}"

def greet_list(names: list[str], greeting_intro: str) -> list[str]:
    """return a list of greeting"""
    return [greet(name, greeting_intro) for name in names]

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
    print(greet(read_name(), read_greeting()))
    print(greet_list(["John", "Jane", "Joe"], read_greeting()))

if  __name__ == "__main__":
    main()