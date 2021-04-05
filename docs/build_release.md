## Setup 
Make sure you install all the dependencies before you begin with the build/release process. Build is used to generate the required files, and twine is used to upload those files to PyPi.
```python
python3 -m pip install --user --upgrade build
python3 -m pip install --user --upgrade twine
```
Then make sure you are in the base directory for this repo.

## Build
Building the program will create two files under dist/ "the tar.gz file is a Source Archive whereas the .whl file is a Built Distribution" [Source].(https://packaging.python.org/tutorials/packaging-projects/) In the repository root directory run:
```bash
python3 -m build
```

## Versioning
Whenever you build your package needs to have a version, you specify this in setup.py using this syntax
```python
setup(
    version = "0.0.2",
    # Other settings...
```
When you are installing locally there is no need to change this version, however, when you upload to PyPi the version must be increased each time or the upload will fail. Because of this we want to avoid uploading to PyPi too often. To test your changes always run them locally until they are completely finished, and if you need to try uploading to the cloud, use Test PyPi instead of the offical PyPi. Having control over what is available to the public ensures that if they go back to a previous version it will still run.

## Install Locally
To install this wheel locally for testing all you need to do is install the wheel through pip.
```bash
pip3 install dist/[wheel_file_name].whl --user --upgrade
```
Now when you run ```import ctf``` this will be your latest version.

## Upload to Test PyPi
TestPyPi is a test version of PyPi that you can upload and install test packages to and from. Use this package index for getting up to speed before uploading to PyPi.
```bash
python3 -m twine upload --repository testpypi dist/*
```

## Upload to PyPi
For uploading to the official Python Package Index PyPi use ```python3 -m twine upload dist/*``` Remember to update the version if this fails to publish.