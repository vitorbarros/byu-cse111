""""
The size of a car tire in the United States is represented with three numbers
like this: 205/60R15. The first number is the width of the tire in millimeters.
The second number is the aspect ratio.
The third number is the diameter in inches of the wheel that the tire fits.
"""

import math
import os
from datetime import datetime


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


def get_data():
    return datetime.now()


class WriteFile:

    def __init__(self, t_content):
        self.content = t_content
        self.file_name = 'volumes.txt'
        self.current_path = os.path.dirname(__file__)
        self.file_path = f'{self.current_path}/{self.file_name}'

    def should_generate_heading(self):
        should_generate = True
        with open(self.file_path) as f:
            for index, line in enumerate(f):
                if index > 0:
                    should_generate = False

        return should_generate

    def new_line(self):
        with open(self.file_path, mode='at') as f:
            if self.should_generate_heading():
                print('date,width,aspect_ration,diameter,volume', file=f)

            print(f'{get_data()},{self.content}', file=f)
            print(f'new line appended successfully in {self.file_path}')


width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

tire = Tire(t_width=width, t_diameter=diameter, t_aspect_ratio=aspect_ratio)
volume = tire.volume()

write_file = WriteFile(t_content=f'{width},{aspect_ratio},{diameter},{volume:.2f}')

print(f'The approximate volume is {volume:.2f} liters')

write_file.new_line()
