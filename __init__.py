import os
import json
from cudatext import *
from . import vbscriptbeautifier as v
from . import format_proc

format_proc.INI = 'cuda_vbscript_format.json'
format_proc.MSG = '[VBScript Format] '

def options():

    op = v.default_options()
    fn = format_proc.ini_filename()
    if not os.path.isfile(fn):
        return op

    with open(fn) as f:
        d = json.load(f)
        op.indent_size = d.get("indent_size", 1)
        op.indent_char = d.get("indent_char", "\t")
        op.indent_with_tabs = d.get("indent_with_tabs", True)
        op.preserve_newlines = d.get("preserve_newlines", True)
        op.max_preserve_newlines = d.get("max_preserve_newlines", 10)
    return op


def do_format(text):

    return v.beautify(text, options())


class Command:

    def config_global(self):

        format_proc.config_global()

    def config_local(self):

        format_proc.config_local()

    def run(self):

        format_proc.run(do_format)
