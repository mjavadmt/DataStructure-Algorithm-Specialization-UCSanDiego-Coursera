# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.word_dict = {}
        for i in range(bucket_count):
            self.word_dict[i] = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(reversed(self.word_dict[query.ind]))
        else:
            compute_hash = self._hash_func(query.s)
            if query.type == "add":
                if query.s not in self.word_dict[compute_hash]:
                    self.word_dict[compute_hash].append(query.s)
            elif query.type == "find":
                if query.s not in self.word_dict[compute_hash]:
                    print("no")
                else:
                    print("yes")
            elif query.type == "del":
                if query.s in self.word_dict[compute_hash]:
                    self.word_dict[compute_hash].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
