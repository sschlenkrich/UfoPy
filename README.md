# UfoPy
Example package to test Python packaging and documentation

## Preparations

We setup a conda/pip environment with the package [requirements](./requirements.txt).

```
conda create -n UfoPy Python pytest QuantLib-Python
conda activate UfoPy
pip install xloil
```

In addition we add the following packages (via pip).

```
pip install hatch
pip install --upgrade build
pip install --upgrade twine
pip install -U sphinx
pip install --upgrade myst-parser
```

## Packaging

We follow the guide [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/).


We use [Hatchling](https://hatch.pypa.io/latest/) as build backend.

We need the [pyproject.toml](./pyproject.toml) file with hatchling specification.

Build the package via

```
python -m build
```

Register at [TestPypi](https://test.pypi.org/).

Create an access token [here](https://test.pypi.org/manage/account/#api-tokens)

Upload the package via

```
python -m twine upload --repository testpypi --verbose  dist/*
```

Copy paste access token via right-click in cmd.

Successful upload should be confirmed on command line.

Download and install package via

```
pip install -i https://test.pypi.org/simple/  --no-deps UfoPy-sschlenkrich
```

Test package.

```
python

import UfoPy
```

May throw error due to missing packages because of `--no-deps` option.

Alternatively, install package from local wheel.

```
pip install .\dist\ufopy_sschlenkrich-0.0.1-py3-none-any.whl
```

## Documentation

Setup folders and files via

```
sphinx-quickstart
```

This generates a template using a root file `index.rst`.

To use Markdown source (instead of RST), we install `myst-parser` do the following adjustments to `conf.py`.

```
extensions = ['myst_parser']
```

Remove the `index.rst` file and replace it by Markdown files.

```
index.md
some_feature.md
another_feature.md
```

Add the github action in `documentation.yml`.

Enable Github Pages in repo settings:

- Deploy from branch.
- Use gh-pages branch.

On push, `documentation` and `pages-build-deployment` actions should run.


[![Documentation](https://img.shields.io/badge/Documentation-dev-blue)](https://sschlenkrich.github.io/UfoPy/)