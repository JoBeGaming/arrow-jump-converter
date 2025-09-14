# Config.py
# Configure the converter to your liking.

# (c) JoBe, 2025


# Opcode of instructions that can jump (UPPER, even though instructions can be both)
JUMP_INSTRUCTIONS: dict[str, int] = {"BRH": 2, "JMP": 1}

# Comment delimiter 
# Comments will then be spelled as:
# <code> <COMMENT>...\n
COMMENT: str = ";"

# Placeholder for the address destination.
TARGET_PLACEHOLDER: str = "[address]"

# Symbols for arrows.
PIPE: str = "|"
DASH: str = "-"
ARROW: str = "<"
