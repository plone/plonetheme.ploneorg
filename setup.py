from setuptools import setup, find_packages
setup(
    name='plonetheme.ploneorg',
    packages=find_packages(),
    namespace_packages=[
        'plonetheme',
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone', 
    }
)
