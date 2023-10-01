#!/usr/bin/python3
# 4-inherits_from.py
"""Defines a class-checking function."""

def inherits_from(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
