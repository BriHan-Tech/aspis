import inspect


def num_params(fn):
    signature = inspect.signature(fn)
    params = signature.parameters
    return len(params)
