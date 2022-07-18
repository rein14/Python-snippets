class Vehicle:
    
    def __init__(self, name: str, veh_type:str, contents: list):
        self.name = name
        self.veh_type = veh_type
        self.contents = contents
    
    @classmethod
    def create_method(cls, name):
        return cls(name, veh_type="", contents=[])
    
    @classmethod
    def create_with_contents(cls, name, contents):
        return cls(name, veh_type="", contents=list(contents))

if __name__ == "__main__":
    v = Vehicle.create_method(name="Car")
    print(f"{v.name}")
    v2 = Vehicle.create_with_contents("truck", {"box", "tools"})
    print(f"{v2.name} {v2.contents}")