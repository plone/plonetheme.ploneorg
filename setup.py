from setuptools import find_packages
from setuptools import setup
import os

VERSION='0.0.5'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description='Plone.org theme',
    classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone', 
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    keywords='plone theme zope',
    license='GPL2',
    long_description=(
        open('README.rst').read() +
        open(os.path.join('docs', 'HISTORY.txt')).read()
    ),
    name='plonetheme.ploneorg',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
    test_suite='plonetheme.ploneorg.tests.test_suite',
    url='https://github.com/plone/plonetheme.ploneorg',
    version=VERSION,
    zip_safe=False,
)
