# Changelog

## [Unreleased](https://github.com/dj-wasabi/dj-wasabi-release/tree/HEAD)

[Full Changelog](https://github.com/dj-wasabi/dj-wasabi-release/compare/0.2.0...HEAD)

**Implemented enhancements:**

- Added Sphinx for docs generation [\#33](https://github.com/dj-wasabi/dj-wasabi-release/pull/33) ([dj-wasabi](https://github.com/dj-wasabi))
- Added small description in scripts [\#32](https://github.com/dj-wasabi/dj-wasabi-release/pull/32) ([dj-wasabi](https://github.com/dj-wasabi))
- Added basic check to verify existing keys in dict [\#31](https://github.com/dj-wasabi/dj-wasabi-release/pull/31) ([dj-wasabi](https://github.com/dj-wasabi))
- Added image to be used as part of readme document [\#30](https://github.com/dj-wasabi/dj-wasabi-release/pull/30) ([dj-wasabi](https://github.com/dj-wasabi))

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
