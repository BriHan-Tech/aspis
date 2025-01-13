import re


class ArityError(TypeError):
    def __init__(self, e: Exception):
        super().__init__(str(e))

        self.is_arity_error = False

        self.underapplied = False
        self.overapplied = False
        self.kwarg_error = False
        self.unexpected_kwargs = []

        self._parse_error(e)

    def _parse_error(self, e: Exception):
        if not isinstance(e, TypeError):
            return

        message = str(e.args[0]).lower()

        arg_error_patterns = [
            (r"expected (\d+) arguments?,? got (\d+)", self._match_expected_received),
            (r"takes (\d+) positional arguments? but (\d+) were given", self._match_expected_received),
            (
                r"missing (\d+) required positional arguments?: ((?:'[\w_]+'(?:, )?)+)",
                self._handle_underapplication_args,
            ),
            (r"must have at least (\w+) arguments.", self._handle_underapplication_args),
            (r"got multiple values for argument '(.*?)'", self._handle_overapplication_args),
        ]

        kwarg_error_patterns = [
            (
                r"missing (\d+) required keyword-only arguments?: ((?:'[\w_]+'(?:, )?)+)",
                self._handle_underapplication_args,
            ),
            (r"got an unexpected keyword argument '(.*?)'", self._handle_overapplication_kwargs),
        ]

        for pattern, handler in arg_error_patterns + kwarg_error_patterns:
            match = re.search(pattern, message)

            if match:
                self.is_arity_error = True
                handler(match)
                break

    def _match_expected_received(self, match):
        if int(match.group(1)) > int(match.group(2)):
            self._handle_underapplication_args(match)
        else:
            self._handle_overapplication_args(match)

    def _handle_underapplication_args(self, _):
        self.underapplied = True

    def _handle_overapplication_args(self, _):
        self.overapplied = True

    def _handle_underapplication_kwargs(self, _):
        self.underapplied = True
        self.kwarg_error = True

    def _handle_overapplication_kwargs(self, match):
        self.overapplied = True
        self.kwarg_error = True
        self.unexpected_kwargs.append(match.group(1))

    def __bool__(self):
        return self.is_arity_error
