
# package/__init__.py
__all__ = ['MODULE1', 'MODULE2', 'MODULE3', 'MODULE4']

from . import MODULE1
from . import MODULE2
from . import MODULE3
from . import MODULE4

def run_module(input_text):
    for module in [MODULE1, MODULE2, MODULE3, MODULE4]:
        if module.process(input_text):
            break  # Exit if one module has handled the input
