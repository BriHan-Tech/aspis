import re


class ArityError(Exception):
    def __init__(self, e: Exception):
        super().__init__(str(e))

        self.is_arity_error = False
        self.expected = 0
        self.received = 0
        self._parse_error(e)

    def _parse_error(self, e: Exception):
        if not isinstance(e, TypeError):
            return

        message = str(e.args[0]).lower()

        patterns = [
            (r"expected (\d+) arguments?,? got (\d+)", self._match_expected_received),
            (r"missing (\d+) required positional arguments?", self._handle_missing_args),
            (r"missing (\d+) required positional argument: '(\w+)'", self._handle_missing_args),
            (r"takes (\d+) positional arguments? but (\d+) were given", self._match_expected_received),
        ]

        for pattern, handler in patterns:
            match = re.search(pattern, message)

            if match:
                handler(match)
                break

    def _match_expected_received(self, match):
        self.is_arity_error = True
        self.expected = int(match.group(1))
        self.received = int(match.group(2))

    def _handle_missing_args(self, match):
        self.is_arity_error = True
        missing = int(match.group(1))
        self.expected = self.received + missing

    def __bool__(self):
        return self.is_arity_error

    def __str__(self):
        if self.is_arity_error:
            return f"Expected {self.expected} arguments, got {self.received}"
        return super().__str__()
