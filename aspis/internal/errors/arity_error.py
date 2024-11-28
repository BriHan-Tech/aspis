import re


class ArityError(TypeError):
    def __init__(self, e: Exception):
        super().__init__(str(e))

        self.is_arity_error = False

        # NOTE: expected and received do not reflect the number of arguments expected and received
        self.expected = 0
        self.received = 0

        self._parse_error(e)

    def _parse_error(self, e: Exception):
        if not isinstance(e, TypeError):
            return

        message = str(e.args[0]).lower()

        patterns = [
            (r"expected (\d+) arguments?,? got (\d+)", self._match_expected_received),
            (r"missing (\d+) required positional arguments?: ((?:'[\w_]+'(?:, )?)+)", self._handle_missing_args),
            (
                r"missing (\d+) required keyword-only arguments?: ((?:'[\w_]+'(?:, )?)+)",
                self._handle_missing_args,
            ),
            (r"takes (\d+) positional arguments? but (\d+) were given", self._match_expected_received),
            (r"(\w+)\(\) must have at least (\w+) arguments.", self._expected_more_args),
        ]

        for pattern, handler in patterns:
            match = re.search(pattern, message)

            if match:
                handler(match)
                break

    def _expected_more_args(self, _):
        self.is_arity_error = True
        self.expected = 1
        self.received = 0

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
