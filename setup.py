from setuptools import setup, find_packages


long_description = '''
LASER
=======

LASER is a symbolic Ethereum virtual machine.

Installation and setup
----------------------

Install from Pypi:

.. code:: bash

    $ pip install laser-ethereum

Usage
------------------

The easiest way to use LASER is by installing Mythril command line tool:

.. code:: bash

    $ pip install mythril
    $ myth --init-db
    $ myth --fire-laser -a [contract-address]

'''


setup(
    name='laser-ethereum',

    version='0.1.3',

    description='Symbolic Ethereum virtual machine',
    long_description=long_description,

    author='Bernhard Mueller',
    author_email='bernhard.mueller11@gmail.com',

    license='Free for non-commercial use',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Testing',

        'License :: Free for non-commercial use',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='hacking security ethereum',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'graphviz>=0.8',
        'z3-solver>=4.5'
    ],

    python_requires='>=3.5',

)