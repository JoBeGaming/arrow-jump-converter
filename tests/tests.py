# Tests for the parser

# (c) JoBe, 2025


import sys
import os

# Add the parent path to importable path.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools import (
    replace_ordered,
    show_diff,
)


from ajc import convert
from ajc.config import JUMP_INSTRUCTIONS




JMP = list(JUMP_INSTRUCTIONS.keys())[0]


# -------------------------------------
# TESTS
# -------------------------------------



TestStr1: str = f"""
nap <------------|
jmp [address] ---|-----------------|
nbp              |                 |
ncp <------------|-----------------|
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

SUB r0 r3 r0     <--------------|
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
SUB r0 r2 r4                    |
BRH ge [address] ---------------|
"""

TestRes3: str = replace_ordered(TestStr3, ["16", "21", "7"])


if __name__ == "__main__":
    for s, r in (
        (TestStr1, TestRes1),
        (TestStr2, TestRes2),
        (TestStr3, TestRes3)
    ):
        if diff := show_diff(convert(s.split("\n")), r.split("\n")):
            print(diff)
