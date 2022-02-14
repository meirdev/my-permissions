from setuptools import setup, find_packages

from my_permissions import __version__

URL = "https://github.com/meirdev/my-permissions"
PYTHON_REQUIRES = ">=3.7"

setup(
    name="my_permissions",
    url=URL,
    python_requires=PYTHON_REQUIRES,
    version=__version__,
    packages=find_packages(),
    entry_points={"console_scripts": ["mypermissions = my_permissions.__main__:main"]},
    install_requires=["rich"],
)
