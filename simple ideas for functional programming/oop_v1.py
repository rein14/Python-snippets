from datetime import datetime
 
class Greeting:
    def __init__(self) -> None:
        current_time = datetime.now()
        if current_time.hour < 12:
            self.greeting_intro = "Good moring"
        elif 12 <= current_time.hour < 18:
            self.greeting_intro = "Good afternoon"
        else:
            self.greeting_intro = "Good evening"

    def greet(self, name:str):
        print(f"{self.greeting_intro}, {name}")

    def greet_list(self, name: list[str]) -> None:
        for name in name:
            self.greet(name)    

def main() -> None:
    name = input("Enter your name: ")

    greeting = Greeting()
    greeting.greet(name)

if  __name__ == "__main__":
    main()