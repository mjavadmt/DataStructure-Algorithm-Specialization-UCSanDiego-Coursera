# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, nex in enumerate(text):
        if nex in "([{":
            opening_brackets_stack.append((i, nex))

        if nex in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            popped = opening_brackets_stack.pop()
            if not are_matching(popped[1], nex):
                return i + 1
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0][0] + 1
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
