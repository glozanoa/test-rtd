"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"

from time import sleep

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None, sleeper: int = 1):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :param sleeper: Time to sleep
    :type sleeper: int
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

def sleeper(seconds: int):
    """
    Slepp by the supplied seconds

    :param seconds: Seconds to sleep
    :type seconds: int
    """
    sleep(seconds)  
