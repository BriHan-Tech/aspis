import operator

from .curry import curry

divide = curry(operator.truediv)
