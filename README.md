# Add fzf-powered ctrl+r to ipython

Add fzf-powered ctrl+r to ipython. It's nice.

## Installation

You must have fzf installed for this to work:

```bash
# macos
brew install fzf

# linux
apt-get install fzf
```

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