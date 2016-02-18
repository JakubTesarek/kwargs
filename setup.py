from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kwargs',
    version='1.0.0',
    description='Python micro-framework',
    long_description=long_description,
    url='https://github.com/JakubTesarek/kwargs',
    author='Jakub Tesárek',
    author_email='mail@jakubtesarek.cz',
    license='GNU GPL v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='framework',
    packages=find_packages(),
    extras_require={
        'test': ['pytest', 'pylint'],
    }
)