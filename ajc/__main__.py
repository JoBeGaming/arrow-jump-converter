# Simple CLI for aj -> normal form.

# (c) JoBe, 2025


import sys


from .converter import convert


def conv(file: str) -> None:
    with open(file, "r") as f:
        lines = convert(f.readlines())
    with open(file, "w") as f:
        f.writelines(lines)


def main(cmd: str, args: list[str]) -> None:
    match cmd:
        case "help":
            print("Please make Jobe do the help text")
        case "conv":
            jargs = "".join(args)
            if "-f" in jargs:
                conv(args[2])
            else:
                print("TODO")
        case _:
            raise ValueError(f"Unknown command '{cmd}'")


if __name__ == "__main__":
    cmd = sys.argv[0]
    args = sys.argv[:1]
    main(cmd, args)
