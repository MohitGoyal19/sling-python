import os
from setuptools import setup
from setuptools import find_packages

version = os.getenv('SLING_VERSION')
if not version:
  raise Exception('version is blank')
elif version == 'dev':
  version='v0.0.dev'

setup(
  name='sling-windows-amd64',
  version=version,
  description='Sling Binary for Windows',
  author='Fritz Larco',
  author_email='fritz@slingdata.io',
  url='https://github.com/slingdata-io/sling-python',
  download_url='https://github.com/slingdata-io/sling-python/archive/master.zip',
  keywords=['sling', 'etl', 'elt', 'extract', 'load'],

  # https://setuptools.pypa.io/en/latest/userguide/datafiles.html#subdirectory-for-data-files
  packages=find_packages(exclude=['tests']),
  long_description_content_type='text/markdown',
  long_description=open(os.path.join(os.path.dirname(__file__), '..', '..', 'README.md')).read(),
  include_package_data=True, # uses MANIFEST.in
  install_requires=[],
  extras_require={},
  entry_points={},
  classifiers=[
    'Programming Language :: Python :: 3', 'Intended Audience :: Developers',
    'Intended Audience :: Education', 'Intended Audience :: Science/Research',
    'Operating System :: MacOS', 'Operating System :: Unix',
    'Topic :: Utilities'
  ])