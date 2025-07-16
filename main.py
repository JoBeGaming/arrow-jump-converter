# arrow jump parser

# (c) JoBe, 2025


from typing import LiteralString


__all__: list[str] = [
    "main", 
    "cleanup", 
    "parse",

    # Note that these are mostly used for testing
    "JUMP_INSTRUCTIONS",
    "TARGET_PLACEHOLDER",
    "COMMENT"
]


JUMP_INSTRUCTIONS: dict[str, int] = {"BRH": 2, "JMP": 1} # Opcode of instructions that can jump (UPPER, even though instructions can be both)
TARGET_PLACEHOLDER: str = "[address]"
COMMENT: str = ";"


def main(file: str) -> None:
    with open(file, "r") as f:
        lines = parse(f.readlines())
    with open(file, "w") as f:
        f.writelines(lines)


def cleanup(line: str) -> str:
    return line.replace("|", "").replace("<", "").replace("-", "").rstrip()


# O(n²) instead of O(n) -> ;(
def parse(lines: list[str] | list[LiteralString]) -> list[str]:
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

        elif not cline.replace(" ", "").replace("\n", "").replace("|", ""):
            del lines[d_idx]
            d_idx -= 1
            continue

    for tline in lines:
        tln = tline.upper().split()

        idx += 1
        d_idx += 1
        if "<" in tline:
            for section in tln:
                if section.startswith("<"):
                    tline = tline.replace("\n", " ")
                    target_depth = len(tline.split("-| ")[0])
                    target = idx

            sub_idx = -1
            for ln in lines:
                if ln:
                    sub_idx += 1

                if TARGET_PLACEHOLDER.upper() in ln.upper():
                    ln = ln.replace("\n", " ")
                    depth = len(ln.split("-| ")[0])
                    if depth == target_depth:
                        ln = ln.replace(TARGET_PLACEHOLDER, str(target))
                        lines[sub_idx] = cleanup(ln) # type: ignore

        else:
            continue

    for fline in lines:
        res.append(cleanup(fline)) # type: ignore

    return res # type: ignore # All this just because `split` returns a LiteralString :(


# Build a simple CLI to run the parser?
if __name__ == "__main__":
    main(input("Please input the file name: "))