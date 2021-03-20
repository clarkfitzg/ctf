## Setup 
Make sure you install all the dependencies before you begin with the build/release process. Build is used to generate the required files, and twine is used to upload those files to PyPi.
```python
python3 -m pip install --upgrade build
python3 -m pip install --user --upgrade twine
```

## Build
Building the program will create two files under dist/ "the tar.gz file is a Source Archive whereas the .whl file is a Built Distribution." [Source](https://packaging.python.org/tutorials/packaging-projects/)
```bash
python3 -m build
```

## Install Locally
To install this wheel locally for testing all you need to do is install the Wheel through pip.
```bash
pip3 install dist/[wheel_file_name].whl --upgrade
```
Now when you run ```import ctf``` this will be your latest version.

## Upload to PyPi
TestPyPi is a test version of PyPi that you can upload and install test packages to and from. Use this for getting up to speed before uploading to PyPi.
```bash
python3 -m twine upload --repository testpypi dist/*
```
For uploading to PyPi use the same command without the repository argument.
```bash
python3 -m twine upload dist/*
```