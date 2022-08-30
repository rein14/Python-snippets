class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_farenheit(self):
        return(self.temperature * 1.8) + 32
    
    @property
    def temperature(self):
        print("Getting temperature...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -274.15:
            raise ValueError("Value must below -274.15")
        self._temperature = value
    

convert = Celsius(30)

print(convert.temperature)
print(convert.to_farenheit())