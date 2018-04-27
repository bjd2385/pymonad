# --------------------------------------------------------
# (c) Copyright 2014 by Jason DeLaat.
# Licensed under BSD 3-clause licence.
# --------------------------------------------------------

from pymonad.Applicative import *
from functools import wraps


def enforce(fn: Callable[[Callable], 'Monad']) -> Callable[[Callable], 'Monad']:
    @wraps(fn)
    def resultant(action: Callable) -> 'Monad':
        result = fn(action)
        if not isinstance(result, Monad):
            raise TypeError("Operator '>>' must return a Monad instance.")
        return result
    return resultant


class Monad(Applicative):
    """
    Represents a "context" in which calculations can be executed.

    You won't create `Monad` instances directly. Instead, sub-classes implement
    specific contexts. Monads allow you to bind together a series of calculations
    while maintaining the context of that specific monad.

    """

    def __init__(self, value: Any) -> None:
        """ Wraps `value` in the Monad's context. """
        super(Monad, self).__init__(value)

    @abstractmethod
    @enforce
    def bind(self, action: Callable) -> 'Monad':
        """ """
        raise NotImplementedError

    def __rshift__(self, function) -> 'Monad':
        """
        The 'bind' operator. The following are equivalent::

            monadValue >> someFunction
            monadValue.bind(someFunction)

        """
        return self.bind(function)