from setuptools import find_packages
from setuptools import setup

VERSION='0.0.1'


setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone', 
    },
    install_requires=[
        'setuptools',
    ],
    name='plonetheme.ploneorg',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
    version=VERSION,
)
