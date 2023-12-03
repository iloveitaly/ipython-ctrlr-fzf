# Add fzf-powered ctrl+r to ipython [![Release Notes](https://img.shields.io/github/release/iloveitaly/ipython-ctrlr-fzf)](https://github.com/iloveitaly/ipython-ctrlr-fzf/releases)[![Downloads](https://static.pepy.tech/badge/ipython-ctrlr-fzf/month)](https://pepy.tech/project/ipython-ctrlr-fzf)[![Python Versions](https://img.shields.io/pypi/pyversions/ipython-ctrlr-fzf)](https://pypi.org/project/ipython-ctrlr-fzf)![GitHub CI Status](https://github.com/iloveitaly/ipython-ctrlr-fzf/actions/workflows/build_and_publish.yml/badge.svg)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Add fzf-powered ctrl+r to ipython. It's nice.

## Installation

You must have fzf installed for this to work:

```bash
# macos
brew install fzf

# linux
apt-get install fzf
```

I'd also recommend installing [bat](https://github.com/sharkdp/bat) for syntax highlighting. It's detected and an advanced preview is shown when available.

Then, install the extension:

```bash
pip install ipython-ctrlr-fzf
```

And in ipython, load the extension:

```shell
%load_ext ipython_ctrlr_fzf
```

Alternatively, you can add the output of the following to your `ipython_config.py`:

```shell
python -m ipython_ctrlr_fzf
```

## Inspiration

* <https://stackoverflow.com/questions/48203949/backward-search-in-ipython-via-fzf>
* <https://github.com/anntzer/ipython-autoimport>

## TODO

- [ ] understand when prompt toolkit is not used in ipython