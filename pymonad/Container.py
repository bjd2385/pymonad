# --------------------------------------------------------
# (c) Copyright 2014 by Jason DeLaat.
# Licensed under BSD 3-clause licence.
# --------------------------------------------------------

from typing import Any


class Container(object):
    """ Represents a wrapper around an arbitrary value and a method to access it. """

    def __init__(self, value: Any) -> None:
        """
        Wraps the given value in the Container.

        `value` is any arbitrary value of any type including functions.

        """
        self.value = value

    def getValue(self) -> Any:
        """ Returns the value held by the Container. """
        return self.value

    def __eq__(self, other: 'Container') -> bool:
        return self.value == other.value
