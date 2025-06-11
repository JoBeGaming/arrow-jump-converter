JUMP_INSTRUCTIONS: tuple[str, ...] = ("BRH",) # Opcode of instructions that can jump
TARGET_POSITION: int = 2 # Second operand
TARGET_PLACEHOLDER: str = "[address]"
COMMENT: str = "#" # Comment Symbol



def main(file: str):
    with open(file, "r") as f:
        lines = parse(f.readlines())
        f.writelines(lines)

def parse(lines: list[str]) -> list[str]:
    targets: dict[int, int] = {} # depth: line

    for index, line in enumerate(lines):
        ln = line.split()
        if ln[-1].startswith("<"):
            depth = len(ln[-1].split(COMMENT)[0])
            targets[depth] = index

    for index, line in enumerate(lines):
        depth = 0
        ln = line.split()
        if (
          ln[0] in JUMP_INSTRUCTION and
          ln[TARGET_POSITION] == TARGET_PLACEHOLDER
        ):
            depth = len(ln[-1].split(COMMENT)[0]
            target = targets[depth]
            line.replace(TARGET_PLACEHOLDER, target)
        lines[index] = line
    
    return lines
