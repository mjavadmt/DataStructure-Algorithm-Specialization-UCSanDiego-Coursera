# python3
import sys

NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4


def traverse_indexes(pattern, tree):
    ind = 0
    for j in range(len(pattern)):
        try:
            ind = tree[ind][pattern[j]]
        except:
            return ind, j

    tree[ind]["is_leaf"] = True
    return ind, j


def build_leaf(ind, j, last_index, tree, pattern):
    for k in range(len(pattern[j:])):
        tree[ind][pattern[j+k]] = last_index + 1
        ind = last_index + 1
        tree[ind] = {"is_leaf": True}
        last_index += 1
    return last_index


def build_trie(patterns):
    tree = dict()
    for j in range(len(patterns[0])):
        tree[j] = {patterns[0][j]: j + 1}
    current_max_idx = len(patterns[0])
    tree[current_max_idx] = {"is_leaf": True}
    for pattern in patterns[1:]:
        ind, j = traverse_indexes(pattern, tree)
        current_max_idx = build_leaf(ind, j, current_max_idx, tree, pattern)
    return tree


def reach_leaf(t, trie):
    s = 0
    for i in t:
        try:
            s = trie[s][i]
            if trie[s] == {} or trie[s]["is_leaf"]:
                return True
        except:
            return False


def solve(text, n, patterns):
    trie = build_trie(patterns)
    results = []
    for i in range(len(text)):
        if reach_leaf(text[i:], trie):
            results.append(i)
    return results

# def solve(text, n, patterns):

#     trie = build_trie(patterns)
#     results = []
#     for i in range(len(text)):
#         leaf = reach_leaf(text[i:], trie)
#         if leaf:

#             results.append(i)
# 	a = 2


solve("ACATA", 3, ["A", "AT", "AG"])
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
