import operator

from .curry import curry

multiply = curry(operator.mul)
