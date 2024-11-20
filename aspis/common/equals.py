import operator

from .curry import curry

equals = curry(operator.eq)
