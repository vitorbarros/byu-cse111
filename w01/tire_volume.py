""""
The size of a car tire in the United States is represented with three numbers
like this: 205/60R15. The first number is the width of the tire in millimeters.
The second number is the aspect ratio.
The third number is the diameter in inches of the wheel that the tire fits.
"""

import math


class Tire:

    def __init__(self, t_width, t_aspect_ratio, t_diameter):
        self.width = t_width
        self.aspect_ratio = t_aspect_ratio
        self.diameter = t_diameter

        self.denominator = 10000000000
        self.calc_const = 2540

    def volume(self):
        numerator_calc = math.pi * pow(self.width, 2) * self.aspect_ratio * (
                self.width * self.aspect_ratio + self.calc_const * self.diameter)

        result = numerator_calc / self.denominator

        return result


width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

tire = Tire(t_width=width, t_diameter=diameter, t_aspect_ratio=aspect_ratio)

volume = tire.volume()

print(f'The approximate volume is {volume:.2f} liters')
