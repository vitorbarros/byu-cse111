"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

import math

AGE_SUB = 220
MIN_PERCENT_TO_STRENGTHEN = 65
MAX_PERCENT_TO_STRENGTHEN = 85


def calc_heart_rate(age):
    age_number = int(age)
    max_rate = AGE_SUB - age_number

    min_rate_to_strengthen = math.ceil((max_rate / 100) * MIN_PERCENT_TO_STRENGTHEN)
    max_rate_to_strengthen = math.ceil((max_rate / 100) * MAX_PERCENT_TO_STRENGTHEN)

    prompt = f'When you exercise to strengthen your heart, you should\n' \
             f'keep your heart rate between {min_rate_to_strengthen} ' \
             f'and {max_rate_to_strengthen} beats per minute.'

    return prompt


ageInput = input('Please enter your age: ')
result = calc_heart_rate(ageInput)
print(result)
