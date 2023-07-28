#!/usr/bin/env python3

import argparse
import os

stdin = lambda: input("Program requires input: ")[0]
stdout = lambda *args: print(*args, end="")
array_size = 30000


DEBUG = False


def init_list(size):
    arr = []
    for _ in range(size):
        arr.append(0)

    return arr


def parse_input(code):
    commands = []
    stack = []

    for char in code:
        if char in "+-<>.,[]":
            if char not in "[]":
                commands.append(char)
            if char == "[":
                stack.append(len(commands) - 1)
            elif char == "]":
                if not stack:
                    raise ValueError("Mismatched ']' encountered.")
                opening_bracket_index = stack.pop()
                commands[opening_bracket_index + 1] = commands[
                    opening_bracket_index + 1 : len(commands)
                ]
                commands = commands[: opening_bracket_index + 2]

    if stack:
        raise ValueError("Mismatched '[' encountered.")

    return commands


def run_command(cmd, pointer, array):
    global DEBUG
    if DEBUG is True:
        print(f"Current command {cmd}")
        print(f"Current pointer {pointer[0]}")
        print(array[:10])
        input(">")
    if isinstance(cmd, list):
        while array[pointer[0]] != 0:
            for _cmd in cmd:
                run_command(_cmd, pointer, array)

        return
    if cmd == "+":
        array[pointer[0]] += 1
    elif cmd == "-":
        array[pointer[0]] -= 1
    elif cmd == "<":
        pointer[0] -= 1
    elif cmd == ">":
        pointer[0] += 1
    elif cmd == ".":
        stdout(chr(array[pointer[0]]))
    elif cmd == ",":
        array[pointer[0]] = stdin()


def runbf(code, array):
    pointer = [0]

    commands = parse_input(code)

    for cmd in commands:
        run_command(cmd, pointer, array)

    print("\n")


def main():
    global DEBUG
    parser = argparse.ArgumentParser(
        description="A simple brainfuck compiler",
        prog="bf run",
    )

    parser.add_argument("file", help="Path to input file")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument(
        "--array-size",
        type=int,
        help="The size of the array for the program default is 30000",
        default=30000,
    )
    args = parser.parse_args()
    if not os.path.exists(args.file):
        return parser.error(f"File {args.file} does not exist")

    array = init_list(args.array_size)
    DEBUG = args.debug
    with open(args.file, "r") as f:
        file = f.read()

    runbf(file, array)


if __name__ == "__main__":
    main()
