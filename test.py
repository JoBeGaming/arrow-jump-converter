# Tests for the parser

# (c) JoBe, 2025


import collections.abc


from main import parse, cleanup, TARGET_PLACEHOLDER


def replace_ordered(string: str, replacements: collections.abc.Sequence[str], pattern: str = TARGET_PLACEHOLDER) -> str:
    res = ""
    count = 0

    for sub in string.split(pattern, len(replacements)):
        if count >= len(replacements):
            res += "\n".join(clean(s) for s in sub.split("\n")) 

        else:
            res += "\n".join(clean(s) for s in f"{sub}{replacements[count]}".split("\n"))
            count += 1

    return res


def clean(string: str) -> str:
    return cleanup(string)


def show_diff(a: collections.abc.Sequence[str], b: collections.abc.Sequence[str]) -> str:
    res: list[str] = []
    for sub_a, sub_b in zip(a, b):

        if sub_a != sub_b: 
            res.append(f"\033[31m{sub_a} <> {sub_b}\033[0m")

        else: 
            res.append(sub_a)

    return "\n".join(res)

# -------------------------------------
# TESTS
# -------------------------------------



TestStr1: str = f"""
nop <------------|
jmp [address] ---|-----------------|
nop              |                 |
nop <------------|-----------------|
brh 0 [address] -|
"""

TestRes1: str = replace_ordered(TestStr1, ["3", "0"])


TestStr2: str = f"""
nop
"""

TestRes2: str = TestStr2


TestStr3 = """
LDI r1 [radius]
LDI r5 246
LDI r6 247
ADD r2 r1 r0

SUB r3 r1 r0
ADD r3 r1 r1
ADI r3 3

SUB r0 r3 r0 //  <--------------|
BRH neg [address] ------|       |
ADI r2 255              |       |
SUB r7 r2 r4            |       |
ADD r7 r7 r7            |       |
ADD r7 r7 r7            |       |
ADI r7 10               |       |       
ADD r3 r3 r7            |       |
JMP [address] ----------|--|    | 
                        |  |    |
ADD r7 r4 r0 <----------|  |    |
ADD r7 r7 r7               |    |
ADD r7 r7 r7               |    |
ADI r7 6                   |    |
ADD r3 r3 r7               |    |
                           |    |
LDI r7 0 <-----------------|    |
ADI r4 1                        |
STR r4 0 r5                     |
STR r2 0 r6                     |
                                |
STR r4 0 r6                     |
STR r2 0 r5                     |
SUB r8 r4 r0                    |
STR r8 0 r5                     |
STR r2 0 r6                     |
                                |
STR r8 0 r6                     |
STR r2 0 r5                     |
SUB r9 r2 r0                    |
STR r8 0 r5                     |
STR r9 0 r6                     |
                                |
STR r8 0 r6                     |
STR r9 0 r5                     |
                                |
STR r4 0 r5                     |
STR r9 0 r6                     |
                                |
STR r4 0 r6                     |
STR r9 0 r5                     |
                                |
SUB r0 r2 r4 //                 |
BRH ge [address] ---------------|
"""

TestRes3: str = replace_ordered(TestStr3, ["16", "21", "7"])


if __name__ == "__main__":
    assert parse(TestStr1.split("\n")) == TestRes1.split("\n")
    assert parse(TestStr2.split("\n")) == TestRes2.split("\n")
    print(show_diff(TestRes3.split("\n"), parse(TestStr3.split("\n"))))
    exit()
    assert parse(TestStr3.split("\n")) == TestRes3.split("\n")