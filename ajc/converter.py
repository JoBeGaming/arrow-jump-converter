# converter of AJ -> Normal form.

# (c) JoBe, 2025


from typing import LiteralString


from .config import (
    ARROW,
    COMMENT, 
    DASH,
    PIPE,
    TARGET_PLACEHOLDER
)

from .tools import cleanup


__all__ = [
    "convert"
]


# TODO: Make this be O(n) instead of O(n²)
def convert(lines: list[str] | list[LiteralString]) -> list[str]:
    res: list[str] = []
    idx = -1
    d_idx = 0
    target_depth = 0
    target = 0

    for cline in lines:
        cln = cline.upper().split()

        if not cln or cln[0].startswith(COMMENT):
            del lines[d_idx]
            d_idx -= 1
            continue

        elif not cline.replace(" ", "").replace("\n", "").replace(PIPE, ""):
            del lines[d_idx]
            d_idx -= 1
            continue

    for tline in lines:
        tln = tline.upper().split()

        idx += 1
        d_idx += 1
        if ARROW in tline:
            for section in tln:
                if section.startswith(ARROW):
                    tline = tline.replace("\n", " ")
                    target_depth = len(tline.split(f"{DASH}{PIPE} ")[0])
                    target = idx

            sub_idx = -1
            for ln in lines:
                if ln:
                    sub_idx += 1

                if TARGET_PLACEHOLDER.upper() in ln.upper():
                    ln = ln.replace("\n", " ")
                    depth = len(ln.split(f"{DASH}{PIPE} ")[0])
                    if depth == target_depth:
                        ln = ln.replace(TARGET_PLACEHOLDER, str(target))
                        lines[sub_idx] = cleanup(ln) # type: ignore

        else:
            continue

    for fline in lines:
        res.append(cleanup(fline))

    return res
