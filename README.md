# Aspis

Aspis is a small functional programming toolkit for Python.  It provides
common helpers such as `curry`, `compose` and `pipe` that make it easier to
build declarative data pipelines.

Documentation for all modules is available on the project website.  The site is
generated from the package's docstrings using Sphinx.

### Building the documentation locally

```bash
cd docs
make html
```

The resulting site will be available in `docs/build/html`.

### Installation

```bash
pip install aspis
```

### Running the tests

```bash
pytest
```

## License

This project is licensed under the MIT License.
