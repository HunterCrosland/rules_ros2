""" Fakes necessary interfaces of the original library.
"""

from .packages import *


def get_resources(*_):
    """ Fix when needed.
    """
    return dict()


def get_packages_with_prefixes(*_):
    """ Fix when needed.
    """
    return None