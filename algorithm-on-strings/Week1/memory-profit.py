# python3
import sys
from queue import Queue


class Edge:
    def __init__(self, character, index_char):
        self.character = character
        self.index_char = index_char

    def __eq__(self, value):
        return self.character == value.character

    def __hash__(self):
        return ord(self.character)

    def __repr__(self):
        return f"{self.character} {self.index_char}"

# e1 = Edge("B" , 3)
# e2 = Edge("B" , 4)
# d = {e1 : "slm"}
# print(d[e2])


def traverse_indexes(pattern, tree):
    ind = 0
    for j in range(len(pattern)):
        try:
            e = Edge(pattern[j], j)
            ind = tree[ind][e]
        except:
            return ind, j
    return ind, j


def build_leaf(ind, i, j, last_index, tree, pattern):
    for k in range(len(pattern[j:])):
        e = Edge(pattern[j+k], i + j + k)
        tree[ind][e] = last_index + 1
        ind = last_index + 1
        tree[ind] = {}
        last_index += 1
    return last_index


def build_trie(text):
    tree = dict()
    for j in range(len(text)):
        e = Edge(text[j], j)
        tree[j] = {e: j + 1}
    current_max_idx = len(text)
    tree[current_max_idx] = {}
    for i in range(1, len(text)):
        subtext = text[i:]
        ind, j = traverse_indexes(subtext, tree)
        current_max_idx = build_leaf(ind, i, j, current_max_idx, tree, subtext)
    new_tree = SuffixTree()
    BFS_shorten_tree(tree, 0, new_tree)
    tree.clear()
    leaves = []
    for i in new_tree.leaves:
        for j in new_tree.leaves[i]:
            leaves.append(text[j[0]:j[0] + j[1]])
    return leaves


def how_far_can_go(tree, idx):
    # make_str = ""
    how_much = 1
    while len(list(tree[idx].keys())) == 1:
        # make_str += list((tree[idx].keys()))[0]
        idx = tree[idx][list((tree[idx].keys()))[0]]
        how_much += 1
        if tree[idx] == {}:
            return idx, how_much
    return idx, how_much


def shorten_tree(tree, start_index, new_tree):
    new_tree.leaves[start_index] = {}
    for i in tree[start_index]:
        idx, how_much = how_far_can_go(tree, tree[start_index][i])
        new_tree.leaves[start_index][(i.index_char, how_much)] = idx
        shorten_tree(tree, idx, new_tree)


def BFS_shorten_tree(tree, start_index, new_tree):
    q = Queue()
    q.put(start_index)
    while not q.empty():
        dequeued = q.get()
        new_tree.leaves[dequeued] = {}
        for edge in tree[dequeued]:
            idx, how_much = how_far_can_go(tree, tree[dequeued][edge])
            new_tree.leaves[dequeued][(edge.index_char, how_much)] = idx
            q.put(idx)
    c = 2


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
