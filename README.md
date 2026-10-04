# portable-tree

Read-only cross-platform filename collision and portability audit.

An offline Python 3.10+ MVP with no runtime dependencies.

## Install and first useful result

```sh
git clone https://github.com/nripankadas07/portable-tree.git
cd portable-tree
python -m venv .venv
# POSIX; on Windows use .venv\Scripts\activate
. .venv/bin/activate
python -m pip install .
portable-tree --help
python demo.py
```

The demo creates temporary synthetic inputs and prints the actual report; it does not require accounts, services, API keys or user data. CLI exit status: 0 = accepted/clean; 1 = review findings; 2 = invalid input or operational error.

## CLI example

```sh
portable-tree ./release-tree
```

Pass an existing directory. The audit reports findings and does not rename files or follow symlinks.

## Validate

```sh
python -m unittest discover -v
python -m compileall -q portable_tree.py
python demo.py
```

## Limits

Reports a conservative portability subset. Does not rename files, simulate every filesystem, check total path lengths, or follow symlink targets. The root must be trusted; directory scans are not isolated from concurrent filesystem changes.

See [RESEARCH.md](RESEARCH.md) for the user brief and dated comparisons, [VALIDATION.md](VALIDATION.md) for exact check coverage, and [SUPPORT.md](SUPPORT.md) for contributions and security reporting. MIT licensed; original implementation, with standard-library dependencies. No competitor code or prose copied.
