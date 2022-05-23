def __toFahrenheit__(grade, scale):
    if scale == "C":
        result = (grade * 1.8) + 32
    elif scale == "K":
        result = 1.8 * (grade - 273.15) + 32
    else:
        result = grade
    return result


def __toCelsius__(grade, scale):
    if scale == "F":
        result = (grade - 32) * 0.555555559
    elif scale == "K":
        result = (grade - 273.15)
    else:
        result = grade
    return result


def __toKelvin__(grade, scale):
    if scale == "C":
        result = (grade + 273.15)
    elif scale == "F":
        result = 5 / 9(grade - 32) + 273.15
    else:
        result = grade
    return result


class Temperature:

    def __init__(self, Grade, Scale):
        self.grade = Grade
        self.scale = Scale

    def __add__(self, other):
        if isinstance(other, Temperature):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.scale = "No valid"

            return Temperature(round(self.grade + result, 2), self.scale)
        else:
            return "No Valid"

    def __substractBy__(self, other):
        if isinstance(other, Temperature):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.scale = "No valid"

            return Temperature(round(self.grade - result, 2), self.scale)
        else:
            return "No Valid"

    def __divideBy__(self, other):
        if isinstance(other, Temperature):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.scale = "No valid"

            return Temperature(round(self.grade / result, 2), self.scale)
        else:
            return "No Valid"

    def __multiplicateBy__(self, other):
        if isinstance(other, Temperature):
            if self.scale == "F":
                result = __toFahrenheit__(other.grade, other.scale)
            elif self.scale == "C":
                result = __toCelsius__(other.grade, other.scale)
            elif self.scale == "K":
                result = __toKelvin__(other.grade, other.scale)
            else:
                result = 0
                self.scale = "No valid"

            return Temperature(round(self.grade * result, 2), self.scale)
        else:
            return "No Valid"
