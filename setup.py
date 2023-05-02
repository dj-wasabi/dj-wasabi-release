import setuptools
import os

if 'CURRENT_BRANCH' in os.environ:
    current_branch = os.environ["CURRENT_BRANCH"]
else:
    current_branch = 'main'

if 'CURRENT_TAG' in os.environ:
    current_tag = os.environ["CURRENT_TAG"]
    _new_tag = current_tag.split('.')
    new_tag = "{m}.{i}.{p}".format(m=_new_tag[0], i=_new_tag[1], p=int(_new_tag[2]) + 1)

if current_branch != "main":
    latest_tag =new_tag

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'dj-wasabi',
  packages = ['djWasabi'],
  version = latest_tag,
  license='MIT',
  description = 'My personal PIP package',
  long_description = '',
  long_description_content_type = '',
  author = 'Werner Dijkerman',
  author_email = 'iam@werner-dijkerman.nl',
  url = 'https://github.com/dj-wasabi/dj-wasabi-release',
  download_url = 'https://github.com/dj-wasabi/dj-wasabi-release/archive/{u}.tar.gz'.format(u=latest_tag),
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
