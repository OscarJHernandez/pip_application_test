from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()

else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}

with open(os.path.join(_here, 'src_file', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='',
    version=version['__version__'],
    description=('Test pip program'),
    long_description=long_description
    author='Oscar Hernandez',
    author_email='javierhernandezmelgar@gmail.com',
    url='',
    licence='',
    packages=[],
    install_requires=[
        ''
    ],
    include_package_data=True,
    classifiers=[],
)
