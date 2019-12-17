from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='kwargs',
    version='1.0.1',
    python_requires='>=3.6',
    description='Python micro-framework',
    long_description=long_description,
    url='https://github.com/JakubTesarek/kwargs',
    author='Jakub Tesárek',
    author_email='jakub@tesarek.me',
    license='GNU GPL v2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='framework',
    packages=find_packages(),
    extras_require={
        'test': ['pytest', 'pylint', 'pytest-cov'],
    }
)
