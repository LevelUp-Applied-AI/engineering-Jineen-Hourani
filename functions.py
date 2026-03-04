"""
functions.py — Day 7: First Tests

Five functions, each with one bug.
Run `pytest test_functions.py` to see all 5 failures.
Fix each function until the tests pass.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b  # bug: multiplication instead of addition


def is_even(n):
    """Return True if n is even, False if n is odd."""
    return n % 2 == 0  # bug: True for odd numbers, not even


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.

    Formula: (celsius × 9/5) + 32
    """
    return celsius * 9 / 5 + 32 # bug: missing + 32


def count_vowels(s):
    """Return the number of vowels (a, e, i, o, u) in string s.

    Only lowercase vowels are counted.
    """
    return sum(1 for ch in s if ch in "aeiou")  # bug: missing 'a'


def first_word(sentence):
    """Return the first word of a sentence (split on whitespace)."""
    return sentence.split()[0]  # bug: index 1 returns the second word, not the first
