# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pathpattern',
    version='0.0.1',
    description='graph analysis of branching interactive works',
    long_description=readme,
    author='Jeremy Douglass',
    author_email='jeremydouglass@gmail.com',
    url='https://github.com/jeremydouglass/pathpattern',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

