# Changelog

## [0.4.3](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.4.3) (2024-07-13)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.4.2...0.4.3)

**Merged pull requests:**

- Added some more options to http lib [\#54](https://github.com/dj-wasabi/dj-wasabi-release/pull/54) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.4.2](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.4.2) (2024-07-13)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.4.1...0.4.2)

**Implemented enhancements:**

- Automatically increasing version and create a tag [\#52](https://github.com/dj-wasabi/dj-wasabi-release/pull/52) ([dj-wasabi](https://github.com/dj-wasabi))
- Create a Python module and push it to Pypi [\#50](https://github.com/dj-wasabi/dj-wasabi-release/pull/50) ([dj-wasabi](https://github.com/dj-wasabi))

**Fixed bugs:**

- Fix for uploading to Pypi [\#51](https://github.com/dj-wasabi/dj-wasabi-release/pull/51) ([dj-wasabi](https://github.com/dj-wasabi))

**Merged pull requests:**

- Attempt to properly version it [\#53](https://github.com/dj-wasabi/dj-wasabi-release/pull/53) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.4.1](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.4.1) (2021-04-16)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.4.0...0.4.1)

**Merged pull requests:**

- No idea what I did anymore with these changes.. :\) [\#48](https://github.com/dj-wasabi/dj-wasabi-release/pull/48) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.4.0](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.4.0) (2021-03-16)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.3.1...0.4.0)

**Implemented enhancements:**

- Added pre-commit hook to now allow commits into master|main;Moved some tasks before doing an tag [\#47](https://github.com/dj-wasabi/dj-wasabi-release/pull/47) ([dj-wasabi](https://github.com/dj-wasabi))
- Uncomment commit;No None release; Also able to work with https repositories instead of git [\#46](https://github.com/dj-wasabi/dj-wasabi-release/pull/46) ([dj-wasabi](https://github.com/dj-wasabi))
- Added various minor changes [\#45](https://github.com/dj-wasabi/dj-wasabi-release/pull/45) ([dj-wasabi](https://github.com/dj-wasabi))
- Using a class for the HTTP functions [\#43](https://github.com/dj-wasabi/dj-wasabi-release/pull/43) ([dj-wasabi](https://github.com/dj-wasabi))

**Fixed bugs:**

- raise ValueError\('Please provide the owner of the repository.'\) as part of Github Actions execution [\#44](https://github.com/dj-wasabi/dj-wasabi-release/issues/44)

**Security fixes:**

- Bump ansible from 2.9.14 to 2.9.20 [\#49](https://github.com/dj-wasabi/dj-wasabi-release/pull/49) ([dependabot[bot]](https://github.com/apps/dependabot))

## [0.3.1](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.3.1) (2021-02-14)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.3.0...0.3.1)

**Implemented enhancements:**

- Generating documentation automatically when merged on main [\#38](https://github.com/dj-wasabi/dj-wasabi-release/issues/38)

**Fixed bugs:**

- Sphinx 'release' not updated. [\#41](https://github.com/dj-wasabi/dj-wasabi-release/issues/41)

**Merged pull requests:**

- Fixing the path to the file containing the Sphinx configuration [\#42](https://github.com/dj-wasabi/dj-wasabi-release/pull/42) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.3.0](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.3.0) (2021-02-14)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.2.0...0.3.0)

**Implemented enhancements:**

- Usage of a Mock to run some tests specific for doing http requests [\#34](https://github.com/dj-wasabi/dj-wasabi-release/issues/34)
- Update shpinx release when repository contains Sphinx [\#40](https://github.com/dj-wasabi/dj-wasabi-release/pull/40) ([dj-wasabi](https://github.com/dj-wasabi))
- Updating the Sphinx release property file when creating a release [\#39](https://github.com/dj-wasabi/dj-wasabi-release/pull/39) ([dj-wasabi](https://github.com/dj-wasabi))
- Added the usage of python type hinting for all of the functions. [\#35](https://github.com/dj-wasabi/dj-wasabi-release/pull/35) ([dj-wasabi](https://github.com/dj-wasabi))
- Added Sphinx for docs generation [\#33](https://github.com/dj-wasabi/dj-wasabi-release/pull/33) ([dj-wasabi](https://github.com/dj-wasabi))
- Added small description in scripts [\#32](https://github.com/dj-wasabi/dj-wasabi-release/pull/32) ([dj-wasabi](https://github.com/dj-wasabi))
- Added basic check to verify existing keys in dict [\#31](https://github.com/dj-wasabi/dj-wasabi-release/pull/31) ([dj-wasabi](https://github.com/dj-wasabi))
- Added image to be used as part of readme document [\#30](https://github.com/dj-wasabi/dj-wasabi-release/pull/30) ([dj-wasabi](https://github.com/dj-wasabi))

**Fixed bugs:**

- Configured specific Python version for run-me.py script from GH Actions [\#36](https://github.com/dj-wasabi/dj-wasabi-release/pull/36) ([dj-wasabi](https://github.com/dj-wasabi))

**Merged pull requests:**

- Added first test with a mock [\#37](https://github.com/dj-wasabi/dj-wasabi-release/pull/37) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.2.0](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.2.0) (2021-02-01)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.1.0...0.2.0)

**Implemented enhancements:**

- Write the release.sh into Python [\#22](https://github.com/dj-wasabi/dj-wasabi-release/issues/22)
- Able to configure repositories [\#18](https://github.com/dj-wasabi/dj-wasabi-release/issues/18)
- Delete local branches automatically [\#15](https://github.com/dj-wasabi/dj-wasabi-release/issues/15)
- Check if Docker is running before release.py script continues [\#28](https://github.com/dj-wasabi/dj-wasabi-release/pull/28) ([dj-wasabi](https://github.com/dj-wasabi))
- Separating the single big test file into smaller files specific for each module file [\#27](https://github.com/dj-wasabi/dj-wasabi-release/pull/27) ([dj-wasabi](https://github.com/dj-wasabi))
- Improved documentation in doc and script and added a pre-commit hook [\#26](https://github.com/dj-wasabi/dj-wasabi-release/pull/26) ([dj-wasabi](https://github.com/dj-wasabi))
- Added tests and improved the execute command function [\#24](https://github.com/dj-wasabi/dj-wasabi-release/pull/24) ([dj-wasabi](https://github.com/dj-wasabi))
- Added some more tests to increase coverage [\#23](https://github.com/dj-wasabi/dj-wasabi-release/pull/23) ([dj-wasabi](https://github.com/dj-wasabi))

**Fixed bugs:**

- The run-me.py script is failing on executing labels.py script [\#20](https://github.com/dj-wasabi/dj-wasabi-release/issues/20)
- Removing the prints and exit to get the script working again. [\#29](https://github.com/dj-wasabi/dj-wasabi-release/pull/29) ([dj-wasabi](https://github.com/dj-wasabi))

**Merged pull requests:**

- Added the Python script equivalent of the release.sh BASH script [\#25](https://github.com/dj-wasabi/dj-wasabi-release/pull/25) ([dj-wasabi](https://github.com/dj-wasabi))
- Properly able to execute the run-me.py script from GH actions  [\#21](https://github.com/dj-wasabi/dj-wasabi-release/pull/21) ([dj-wasabi](https://github.com/dj-wasabi))
- Added repository script to configure repositories [\#19](https://github.com/dj-wasabi/dj-wasabi-release/pull/19) ([dj-wasabi](https://github.com/dj-wasabi))
- Remove local branches that are already removed on remote [\#17](https://github.com/dj-wasabi/dj-wasabi-release/pull/17) ([dj-wasabi](https://github.com/dj-wasabi))
- Added repository for docker-local-development-puppet [\#14](https://github.com/dj-wasabi/dj-wasabi-release/pull/14) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.1.0](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.1.0) (2021-01-08)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.0.3...0.1.0)

**Implemented enhancements:**

- Added Flake8 pre-commit-hook [\#11](https://github.com/dj-wasabi/dj-wasabi-release/pull/11) ([dj-wasabi](https://github.com/dj-wasabi))
- Add GH Action for generating CHANGELOG [\#10](https://github.com/dj-wasabi/dj-wasabi-release/pull/10) ([dj-wasabi](https://github.com/dj-wasabi))
- Updated versions to be used as part of Molecule runs [\#6](https://github.com/dj-wasabi/dj-wasabi-release/pull/6) ([dj-wasabi](https://github.com/dj-wasabi))
- Create runme script to be executed when merge on master [\#5](https://github.com/dj-wasabi/dj-wasabi-release/pull/5) ([dj-wasabi](https://github.com/dj-wasabi))
- Add Python module incl. tests [\#4](https://github.com/dj-wasabi/dj-wasabi-release/pull/4) ([dj-wasabi](https://github.com/dj-wasabi))

**Fixed bugs:**

- The GH Action `run-all` not working correctly [\#12](https://github.com/dj-wasabi/dj-wasabi-release/issues/12)
- Correcting 'path' to watch for the 'run-all' yob [\#13](https://github.com/dj-wasabi/dj-wasabi-release/pull/13) ([dj-wasabi](https://github.com/dj-wasabi))
- Removal of debug commands [\#9](https://github.com/dj-wasabi/dj-wasabi-release/pull/9) ([dj-wasabi](https://github.com/dj-wasabi))
- Using function to determine github\_user when it is https repo [\#8](https://github.com/dj-wasabi/dj-wasabi-release/pull/8) ([dj-wasabi](https://github.com/dj-wasabi))
- Only execute run when changes are made to a certain paths [\#7](https://github.com/dj-wasabi/dj-wasabi-release/pull/7) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.0.3](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.0.3) (2021-01-01)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.0.2...0.0.3)

**Implemented enhancements:**

- Added first initial attempt to create script to manage labels [\#3](https://github.com/dj-wasabi/dj-wasabi-release/pull/3) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.0.2](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.0.2) (2020-10-17)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.0.1...0.0.2)

**Merged pull requests:**

- Added precommit hook [\#2](https://github.com/dj-wasabi/dj-wasabi-release/pull/2) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.0.1](https://github.com/dj-wasabi/dj-wasabi-release/tree/0.0.1) (2020-10-16)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/cd59e724928d6eb8ff0a701f36835dc28202b9ef...0.0.1)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
