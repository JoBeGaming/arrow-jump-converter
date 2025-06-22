JUMP_INSTRUCTIONS: dict[str, int] = {"BRH": 2, "JMP": 1} # Opcode of instructions that can jump
TARGET_PLACEHOLDER: str = "[address]"
COMMENT: str = "#" # Comment Symbol



def main(file: str) -> None:
    with open(file, "r") as f:
        lines = parse(f.readlines())
    with open(file, "w") as f:
        f.writelines(lines)


def cleanup(line: str) -> str:
    return line.replace("|", "").replace("<", "").replace("-", "")


def parse(lines: list[str]) -> list[str]:
    targets: dict[int, int] = {} # depth: line (target)

    for index, line in enumerate(lines):
        for section in line.split():
            if section.startswith("<"):
                depth = len(line.split("|")[0])
                targets[depth] = index

    for index, line in enumerate(lines):
        depth = 0
        ln = line.split()

        if not ln or ln[0] not in JUMP_INSTRUCTIONS:
            lines[index] = clean(line)
            continue

        if ln[JUMP_INSTRUCTIONS[ln[0]]].startswith(TARGET_PLACEHOLDER):
            depth = len(line.split("|")[0])
            target = targets[depth]
            line = line.replace(TARGET_PLACEHOLDER, str(target))

        lines[index] = cleanup(line)

    return lines


if __name__ == "__main__":
    main(input("Please input the file name: "))
