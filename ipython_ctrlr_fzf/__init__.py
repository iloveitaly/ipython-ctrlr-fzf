from shutil import which
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.keys import Keys
from prompt_toolkit.filters import HasFocus, HasSelection

from pyfzf import pyfzf

fzf = pyfzf.FzfPrompt()


def is_in_empty_line(buf):
    text = buf.text
    cursor_position = buf.cursor_position
    text = text.split("\n")
    for line in text:
        if len(line) >= cursor_position:
            return not line
        else:
            cursor_position -= len(line) + 1


def _install_namespace(ipython):
    def fzf_i_search(event):
        history_set = set()
        history_strings = [i[2] for i in ipython.history_manager.get_tail(5000)][::-1]

        # we replace newlines as fzf can only work on single lines; in the preview and later
        # we reverse this effect
        history_strings = [
            s.replace("\n", " @@ ")
            for s in history_strings
            if not (s in history_set or history_set.add(s))
        ]

        # check if `bat` exists on the system
        preview_command = "cat"

        if which("bat"):
            preview_command = "bat --color=always --style=numbers -l py -"

        # refresh prompt
        print("", end="\r", flush=True)
        try:
            text = fzf.prompt(
                history_strings,
                fzf_options="--no-sort --multi --border --height=80% --margin=1 --padding=1"
                f" --preview 'echo {{}} | sed \"s/ @@ /\\n/g\" | {preview_command}'",
            )
            # multiple returns get concatenated with an emtpy line in-between
            text = "\n\n".join(text)
            # reverse the replacement of newlines
            text = text.replace(" @@ ", "\n")
        except:
            return
        buf = event.current_buffer
        if not is_in_empty_line(buf):
            buf.insert_line_below()
        buf.insert_text(text)

    # Register the shortcut if IPython is using prompt_toolkit
    if getattr(ipython, "pt_app", None):
        registry = ipython.pt_app.key_bindings
        registry.add_binding(
            Keys.ControlR, filter=(HasFocus(DEFAULT_BUFFER) & ~HasSelection())
        )(fzf_i_search)
    else:
        print("ipython_ctrlr_fzf: IPython not using prompt_toolkit, not installing")


def _uninstall_namespace(ipython):
    if getattr(ipython, "pt_app", None):
        registry = ipython.pt_app.key_bindings
        registry.remove_binding(Keys.ControlR)


def load_ipython_extension(ipython):
    _install_namespace(ipython)


def unload_ipython_extension(ipython):
    _uninstall_namespace(ipython)
