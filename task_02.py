import re
from decimal import Decimal
from typing import Callable, Iterable


def generator_numbers(text:str):
    """Takes numbers from a text"""

    # Regular expression to find numbers separated with spaces at both ends
    regex = r'(?<!\S)[+-]?\d+(?:\.\d+)?(?!\S)'

    # Iterate text and extract numbers
    for number in re.finditer(regex, text):
        yield Decimal(number.group())


def sum_profit(text:str, func:Callable[[str], Iterable[Decimal]]):
    """Use generator to calculate sum of profit"""

    # Calculate the total sum of all Decimal numbers returned by generator
    total_income = sum(func(text), Decimal('0.00'))

    return total_income


