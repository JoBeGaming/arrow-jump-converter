# Tests for the parser

# (c) JoBe, 2025


import re
import collections.abc


from main import parse


def replace_in_order(string: str, replacements: collections.abc.Iterable[str], patter: str = ...) -> str:
    repl_iter = iter(replacements)
    
    def repl_func(match):
        try:
            return next(repl_iter)
        except StopIteration:
            return match.group(0)
    
    return re.sub(pattern, repl_func, s)



TestStr1: str = """
"""

TestRes1: str = replace_TestStr1
