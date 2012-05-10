from setuptools import find_packages
from setuptools import setup
import os

VERSION='0.0.2'


setup(
    description='Plone.org theme',
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone', 
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    long_description=(
        open('README.rst').read() +
        open(os.path.join('docs', 'HISTORY.txt')).read()
    ),
    name='plonetheme.ploneorg',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
    version=VERSION,
)
