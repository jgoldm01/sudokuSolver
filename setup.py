from setuptools import setup, find_packages
 
setup(
    name = "eggTest",
    version = "0.1",
    packages = find_packages(),
    data_files =[ ('', ['__main__.py', ]),
    							('', ['frontEnd.py', ]),
    							('', ['solver.py', ])]
    )