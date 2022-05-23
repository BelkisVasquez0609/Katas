from Temperature import Temperature
from TemperatureScalar import TemperatureScalar

if __name__ == '__main__':
     v1 = Temperature(38.4, TemperatureScalar.Celsius)
     v2 = Temperature(93, TemperatureScalar.Fahrenheit)

     v3 = v1.__divideBy__(v2)
     print(f"(Grade: {v3.grade}, Scalar: {v3.scale})")


