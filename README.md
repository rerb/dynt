# Test TV
Django test runner with web interface.

# Requirements

## What's up with `requirements.in` and `requirements_dev.in`?

They're the source for `requirements.txt` and `requirements_dev.txt`
-- those are the compiled results of feeding `requirements.in` and
`requirementst_dev.in` to pip-compile, a command provided by the
pip-tools package..

## Advantages of pip-compiled requirements files.

* All dependencies are marked.  Allows one to clean out old, unneeded
  packages and their dependencies.

## Adding dependencies.

* Add them to requirements.in.

* Regenerate requirements.txt:

```bash
$ pip-compile requirements.in > requirements.txt
```

* Commit the changes to both requirements.in and requirements.txt.

# Installation
