# css-class-names [![Build Status](https://travis-ci.org/arturfsousa/css-class-names.svg?branch=master)](https://travis-ci.org/arturfsousa/css-class-names)

A python script for css class names conditional generation. Inspered by the node package [classnames](https://github.com/JedWatson/classnames).

# Development

After cloning the repository, create a virtualenv and use the `Makefile` commands to `setup` development requirements and run tests:

```bash
make setup
make lint 
make test 
make watch # run tests when code changes
make coverage
```

Alternatively, if you have `tox`, just run `tox` to test everything.
