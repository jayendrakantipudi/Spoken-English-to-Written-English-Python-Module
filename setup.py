import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spk2wrt',
      packages = ['spoken2written'],
      version='0.1',
      license='Licensed by Jayendra Kantipudi',
      description='This module converts spoken english to written english ',
      author='Jayendra Kantipudi',
      author_email='kantipudijayendra@gmail.com',
      url='https://github.com/jayendrakantipudi/Spoken-English-to-Written-English-Python-Module',
      classifiers = [
     					 'Intended Audience :: Developers',
      					'Programming Language :: Python'
  				],
	  long_description='A module that converts spoken english to written english'

     )
