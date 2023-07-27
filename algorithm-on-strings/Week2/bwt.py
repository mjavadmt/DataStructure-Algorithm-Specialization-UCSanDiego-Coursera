# python3
import sys


def generate_sorted_bwt(s):
    l = []
    l.append(s)
    i = len(s) - 1
    while i != 0:
        l.append(s[i:] + s[:i])
        i -= 1
    l.sort()
    return "".join([i[-1] for i in l])
    


def BWT(text):
    return generate_sorted_bwt(text)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
