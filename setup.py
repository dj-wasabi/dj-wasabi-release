import setuptools
import os

version = "0.4.22"

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'dj-wasabi',
  packages = ['djWasabi'],
  version = version,
  license='MIT',
  description = 'My personal PIP package',
  long_description = 'My personal PIP package',
  long_description_content_type = '',
  author = 'Werner Dijkerman',
  author_email = 'iam@werner-dijkerman.nl',
  url = 'https://github.com/dj-wasabi/dj-wasabi-release',
  download_url = 'https://github.com/dj-wasabi/dj-wasabi-release/archive/{u}.tar.gz'.format(u=version),
  keywords = ['personal'],
  package_dir={'': 'lib'},
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
