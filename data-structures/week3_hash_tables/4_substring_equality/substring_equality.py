# python3

import sys


class Solver:
    def __init__(self, s):
        self.s = s
        self.x = 263

    def precompute_hashes(self):
        m1 = 10 ** 9 + 7
        m2 = 10 ** 9 + 9
        h1 = [0 for i in range(len(self.s) + 1)]
        h2 = [0 for i in range(len(self.s) + 1)]
        for j in range(1, len(self.s) + 1):
            h1[j] = (self.x * h1[j - 1] + ord(self.s[j - 1])) % m1
            h2[j] = (self.x * h2[j - 1] + ord(self.s[j - 1])) % m2
        return h1, h2

    def ask(self, a, b, l):
        m1 = 10 ** 9 + 7
        m2 = 10 ** 9 + 9
        h1, h2 = self.precompute_hashes()
        return (h1[a + l] - ((self.x ** l) % m1) * h1[a]) % m1 == (h1[b + l] - ((self.x ** l) % m1) * h1[b]) % m1 and (
                h2[a + l] - ((self.x ** l) % m2) * h2[a]) % m2 == (h2[b + l] - ((self.x ** l) % m2) * h2[b]) % m2


def HashTable(s, prime, x):
    hash_table = [0 for _ in range(len(s) + 1)]
    hash_table[0] = 0
    for i in range(1, len(s) + 1):
        hash_table[i] = (hash_table[i - 1] * x + ord(s[i - 1])) % prime
    return hash_table


def HashValue(hash_table, prime, x, start, length):
    hash_value = (hash_table[start + length] - ((x ** length) % prime) * hash_table[start]) % prime
    return hash_value


def sub_equal(table1, table2, prime1, prime2, x, a, b, l):
    a_hash1 = HashValue(table1, prime1, x, a, l)
    b_hash1 = HashValue(table1, prime1, x, b, l)
    a_hash2 = HashValue(table2, prime2, x, a, l)
    b_hash2 = HashValue(table2, prime2, x, b, l)
    if a_hash1 == b_hash1 and a_hash2 == b_hash2:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    string = input()
    n_queries = int(input())
    m1 = 10**9 + 7
    m2 = 10**9 + 9
    x = 263
    hash_table1 = HashTable(string, m1, x)
    hash_table2 = HashTable(string, m2, x)
    for i in range(n_queries):
        a, b, l = map(int, input().split())
        print(sub_equal(hash_table1, hash_table2, m1, m2, x, a, b, l))

# s1 = Solver("trololo")
# for i in range(4):
#     inp1, inp2, inp3 = map(int, input().split())
#     print(s1.ask(inp1, inp2, inp3))


# s = sys.stdin.readline()
# q = int(sys.stdin.readline())
# solver = Solver(s)
# for i in range(q):
#     a, b, l = map(int, sys.stdin.readline().split())
#     print("Yes" if solver.ask(a, b, l) else "No")
