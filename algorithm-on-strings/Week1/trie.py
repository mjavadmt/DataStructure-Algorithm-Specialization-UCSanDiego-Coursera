# Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.



def traverse_indexes(pattern, tree):
    ind = 0
    for j in range(len(pattern)):
        try:
            ind = tree[ind][pattern[j]]
        except:
            return ind , j
    return ind , j

def build_leaf(ind, j , last_index , tree , pattern):
    for k in range(len(pattern[j:])):
        tree[ind][pattern[j+k]] = last_index + 1
        ind = last_index + 1
        tree[ind] = {}
        last_index += 1
    return last_index

def build_trie(patterns):
    tree = dict()
    for j in range(len(patterns[0])):
        tree[j] = {patterns[0][j]: j + 1}
    current_max_idx = len(patterns[0])
    tree[current_max_idx] = {}
    for pattern in patterns[1:]:
        ind , j = traverse_indexes(pattern, tree)
        current_max_idx = build_leaf(ind , j , current_max_idx , tree , pattern)

    return tree


# patterns = ["AT", "AC", "AG"]
# tree = build_trie(patterns)
# for node in tree:
#     for c in tree[node]:
#         print("{}->{}:{}".format(node, tree[node][c], c))

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
