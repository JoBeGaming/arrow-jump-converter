# Tools used for testing.

# (c) JoBe, 2025


import collections.abc


from ajc.config import TARGET_PLACEHOLDER
from ajc.tools import cleanup



def replace_ordered(string: str, replacements: collections.abc.Sequence[str], pattern: str = TARGET_PLACEHOLDER) -> str:
    res = ""
    count = 0

    for sub in string.split(pattern, len(replacements)):
        if count >= len(replacements):

            subs: list[str] = []
            for s in sub.split("\n"):
                print(s)
                c = clean(s)
                if c.replace(" ", "").replace("\n", ""):
                    subs.append(clean(s))

            res += "\n".join(subs)

        else:

            subs: list[str] = []
            for s in f"{sub}{replacements[count]}".split("\n"):
                print(s)
                c = clean(s)
                if not c.replace(" ", "").replace("\n", ""):
                    subs.append(clean(s))

            print(subs)
            res += "\n".join(subs)
            count += 1

    print(res)
    return res


def clean(string: str) -> str:
    return cleanup(string)


def show_diff(a: collections.abc.Sequence[str], b: collections.abc.Sequence[str]) -> str:
    res: list[str] = []
    count = 0
    msg = f"\n\n\n--- \033[32mNo differences found across {min(len(a), len(b))} pairs\033[0m ---"
    for sub_a, sub_b in zip(a, b):

        if sub_a != sub_b: 
            count += 1
            res.append(f"\033[31m{sub_a} <> {sub_b}\033[0m")

        else: 
            res.append(sub_a)

    if count > 0:
        msg = f"\n\n\n--- \033[31m{count} differences found across {len(res)} pairs\033[0m ---"

    print(a)
    print(b)
    return "\n".join(res) + msg
