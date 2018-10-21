# Publishing

See https://packaging.python.org/tutorials/packaging-projects/

## Steps

```sh
pip install --user --upgrade setuptools wheel
pip install --user --upgrade twine

python setup.py sdist bdist_wheel
twine upload -r pypi dist/*
```

## ~/.pypirc

```ini
[distutils]
index-servers = pypi pypitest

[pypi]
repository: https://upload.pypi.org/legacy/
username: mrts
password: ...

[pypitest]
repository: https://test.pypi.org/legacy/
username: mrts
password: ...
```
