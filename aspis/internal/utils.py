import re


class ArityError(Exception):
    def __init__(self, e: Exception):
        super().__init__(str(e))

        self.is_arity_error = False
        self.expected = 0
        self.received = 0

        if isinstance(e, TypeError):
            pattern = r"expected (\d+) arguments?, got (\d+)"
            match = re.search(pattern, str(e.args[0]).lower())

            if match:
                self.is_arity_error = True
                self.expected = int(match.group(1))
                self.received = int(match.group(2))

    def __bool__(self):
        return self.is_arity_error

    def __str__(self):
        if self.is_arity_error:
            return f"Expected {self.expected} arguments, got {self.received}"
        return super().__str__()


import inspect
from typing import Any, Callable


def get_arity(fn: Callable[..., Any]) -> int:
    signature = inspect.signature(fn)
    params = signature.parameters
    return len(params)
