#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 1 """


def listdivide(numbers, divide=2):
    """
    Returns the number of elements in the
    numbers list that are divisible by divide.
    Args:
        numbers (List): List of integers to test for divisibility
        divide (Int): Integer use for division
    Returns:
        Int: Number of elements divisible by divide.
    Examples:

    """
    items = [x for x in numbers if x % divide == 0]
    return len(items)


class ListDivideException(Exception):
    """ ListDivideException class
    Args:
        Inherited from Exception superclass
    Attributes:
        Inherited from Exception superclass
    Examples:
        >>> raise ListDivideException()
        Traceback (most recent call last):
          File "assignment1_part1.py", line 63, in <module>
            raise ListDivideException()
        __main__.ListDivideException
    """
    pass


def testlistdivide():
    """
    testlistdivide function
    """
    tests = [([1, 2, 3, 4, 5], 2, 2),
             ([2, 4, 6, 8, 10], 2, 5),
             ([30, 54, 63, 98, 100], 10, 2),
             ([], 2, 0),
             ([1, 2, 3, 4, 5], 1, 5)]

    for items, div, res in tests:
        comp = listdivide(items, div)
        if comp != res:
            raise ListDivideException()


if __name__ == '__main__':
    print testlistdivide()