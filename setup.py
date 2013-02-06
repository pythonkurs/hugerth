from setuptools import setup, find_packages
import sys, os

version = '0.3'

setup(name='hugerth',
      version=version,
      description="SciLife python course",
      long_description="",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Luisa Hugerth',
      author_email='luisa.hugerth@scilifelab.se',
      url='https://github.com/pythonkurs.hugerth',
      license='GPL V3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts = ['scripts/getting_data.py', 'scripts/check_repo.py'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'untangle'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
