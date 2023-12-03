import os
import sys


if __name__ == "__main__":
    if os.isatty(sys.stdout.fileno()):
        print(
            """\
# Please append the output of this command to the
# output of `ipython profile locate` (typically
# `~/.ipython/profile_default/ipython_config.py`)

c.InteractiveShellApp.exec_lines.append(
    "try:\\n    %load_ext ipython_ctrlr_fzf\\nexcept ImportError: pass")

"""
        )
