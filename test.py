# Tests for the parser

# (c) JoBe, 2025


import re
import collections.abc


from main import parse, TARGET_PLACEHOLDER


def replace_ordered(string: str, replacements: collections.abc.Iterable[str], patter: str = TARGET_PLACEHOLDER) -> str:
    repl_iter = iter(replacements)
    
    def repl_func(match):
        try:
            return next(repl_iter)
        except StopIteration:
            return match.group(0)
    
    return re.sub(pattern, repl_func, s)



TestStr1: str = f"""
...
"""

TestRes1: str = replace_ordered(TestStr1, [...])


TestStr2: str = f"""
...
"""

TestRes2: str = replace_ordered(TestRes2, [...])



if __name__ == "__main__":
    assert TestStr1 == TestRes1
    assert TestStr2 == TestRes2
    ...
