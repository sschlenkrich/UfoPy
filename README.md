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
