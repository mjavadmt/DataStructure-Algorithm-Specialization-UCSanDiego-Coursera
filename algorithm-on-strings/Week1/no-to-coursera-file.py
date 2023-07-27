#python3
import sys


def traverse_indexes(pattern, tree):
    ind = 0
    for j in range(len(pattern)):
        try:
            ind = tree[ind][pattern[j]]
        except:
            return ind, j
    return ind, j


def build_leaf(ind, j, last_index, tree, pattern):
    for k in range(len(pattern[j:])):
        tree[ind][pattern[j+k]] = last_index + 1
        ind = last_index + 1
        tree[ind] = {}
        last_index += 1
    return last_index


def build_trie(text):
    tree = dict()
    for j in range(len(text)):
        tree[j] = {text[j]: j + 1}
    current_max_idx = len(text)
    tree[current_max_idx] = {}
    for i in range(1, len(text)):
        subtext = text[i:]
        ind, j = traverse_indexes(subtext, tree)
        current_max_idx = build_leaf(ind, j, current_max_idx, tree, subtext)
    new_tree = SuffixTree()
    shorten_tree(tree, 0, new_tree)
    leaves = []
    for i in new_tree.leaves:
        for j in new_tree.leaves[i]:
            leaves.append(j)
    return leaves


def how_far_can_go(tree, idx):
    make_str = ""
    while len(list(tree[idx].keys())) == 1:
        make_str += list((tree[idx].keys()))[0]
        idx = tree[idx][list((tree[idx].keys()))[0]]
        if tree[idx] == {}:
            return idx, make_str
    return idx, make_str


def shorten_tree(tree, start_index, new_tree):
    new_tree.leaves[start_index] = {}
    for i in tree[start_index]:
        idx, make_str = how_far_can_go(tree, tree[start_index][i])
        new_tree.leaves[start_index][i + make_str] = idx
        shorten_tree(tree, idx, new_tree)


class SuffixTree:
    def __init__(self):
        self.leaves = {}
        self.last_index = 0

# build_trie("ATAAATG$")


def build_suffix_tree(text):
    return build_trie(text)


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
