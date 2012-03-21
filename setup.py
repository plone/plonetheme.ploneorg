from setuptools import setup, find_packages
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
    version='0.0.0',
)
