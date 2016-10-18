
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='gap-statistic',
      version='0.1',
      author='Miles Granger',
      author_email='miles.granger@outlook.com',
      description='Python implementation of the gap statistic',
      packages=['gap_statistic'],
      zip_safe=True
      )
