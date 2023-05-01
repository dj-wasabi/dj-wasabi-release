import setuptools
import git

git_repository = git.Repo('.')
git_branch_name = git_repository.active_branch.name
git_tags_all = sorted(git_repository.tags, key=lambda t: t.commit.committed_datetime)
git_tags_latest = git_tags_all[-1]

if git_branch_name != "main":
    latest_tag = "{v}-{b}".format(v=git_tags_latest, b=git_branch_name.replace('/', '-'))

# with open("README.md", "r", encoding = "utf-8") as fh:
#     long_description = fh.read()

# setuptools.setup(
#   name = 'dj-wasabi',
#   packages = ['djWasabi'],
#   version = git_tags_latest,
#   license='MIT',
#   description = 'My personal PIP package',
#   author = 'Werner Dijkerman',
#   author_email = 'iam@werner-dijkerman.nl',
#   url = 'https://github.com/dj-wasabi/dj-wasabi-release',
#   download_url = 'https://github.com/dj-wasabi/dj-wasabi-release/archive/{u}.tar.gz'.format(u=git_tags_latest),
#   keywords = ['personal'],
#   package_dir={'': 'lib'},
#   install_requires=[
#           'requests',
#       ],
#   classifiers=[
#     'Development Status :: 3 - Alpha',
#     'Intended Audience :: Developers',
#     'Topic :: Software Development :: Build Tools',
#     'License :: OSI Approved :: MIT License',
#     'Programming Language :: Python :: 3',
#     'Programming Language :: Python :: 3.9',
#     'Programming Language :: Python :: 3.10',
#   ],
# )
