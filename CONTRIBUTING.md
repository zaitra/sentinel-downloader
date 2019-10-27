# Contributing Guidelines

Thanks for your interest in contributing to `sentinel-downloader`.

The following is a set of guidelines for contributing to `sentinel-downloader`.
Use your best judgement, and feel free to propose changes to this document in a pull request.

By contributing to this project you agree to the Developer Certificate of Origin (DCO). This document is a simple statement that you, as a contributor, have the legal right to submit the contribution. See the [DCO](DCO) file for details.

## Reporting Bugs
Before creating bug reports, please check a [list of known issues](https://github.com/zaitra/sentinel-downloader/issues) to see
if the problem has already been reported (or fixed in a master branch).

If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/zaitra/sentinel-downloader/issues/new).
Be sure to include a **descriptive title and a clear description**. Ideally, please provide:
 * version of sentinel-downloader you are using (`pip3 freeze | grep sentinel-downloader`)
 * the command you executed and a debug output (using option `--debug`)

If possible, add a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

**Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.
You can also comment on the closed issue to indicate that upstream should provide a new release with a fix.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.
When you are creating an enhancement issue, **use a clear and descriptive title** and **provide a clear description of the suggested enhancement** in as many details as possible.

## Guidelines for Developers

If you would like to contribute code to the `sentinel-downloader` project, this section is for you!

### Is this your first contribution?

Please take a few minutes to read GitHub's guide on [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).
It's a quick read, and it's a great way to introduce yourself to how things work behind the scenes in open-source projects.

### Dependencies

If you are introducing a new dependency, please make sure it's added to:
 * [setup.cfg](setup.cfg)

### Documentation

If you want to update documentation, [README.md](README.md) is the file you're looking for.


### Testing

Tests are stored in [tests](/tests) directory.

Running tests locally:
```
make check
```

Running tests in container:
```
make check-in-container
```

### Makefile

#### Requirements

- [docker](https://github.com/moby/moby)

#### Targets

Here are some important and useful targets of [Makefile](/Makefile):

Use [docker](https://github.com/moby/moby) to build container image:
```
make build
```

Try sentinel downloader in container:
```
make run-in-container
```

### How to contribute code to sentinel-downloader

1. Create a fork of the `sentinel-downloader` repository.
2. Create a new branch just for the bug/feature you are working on.
3. Once you have completed your work, create a Pull Request, ensuring that it meets the requirements listed below.

### Requirements for Pull Requests

* Please create Pull Requests against the `master` branch.
* Please make sure that your code complies with [PEP8](https://www.python.org/dev/peps/pep-0008/).
* One line should not contain more than 100 characters.
* Make sure that new code is covered by a test case (new or existing one).
* The tests have to pass.

### Checkers/linters/formatters & pre-commit

To make sure our code is compliant with the above requirements, we use:
* [black code formatter](https://github.com/ambv/black)
* [Flake8 code linter](http://flake8.pycqa.org)
* [mypy static type checker](http://mypy-lang.org)

There's a [pre-commit](https://pre-commit.com) config file in [.pre-commit-config.yaml](.pre-commit-config.yaml).
To [utilize pre-commit](https://pre-commit.com/#usage), install pre-commit with `pip3 install pre-commit` and then either
* `pre-commit install` - to install pre-commit into your [git hooks](https://githooks.com). pre-commit will now run all the checkers/linters/formatters on every commit.
* Or if you want to manually run all the checkers/linters/formatters, run `pre-commit run --all-files`.

Thank you for your interest!
