class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_root = self.get_parent(src)
        dest_root = self.get_parent(dst)

        if src_root == dest_root:
            return False
        if self.ranks[src_root] >= self.ranks[dest_root]:
            self.parents[src_root] = dest_root
        else:
            self.parents[dest_root] = src_root
            if self.ranks[src_root] == self.ranks[dest_root]:
                self.ranks[src_root] += 1

        self.row_counts[dest_root] += self.row_counts[src_root]
        self.row_counts[src_root] = 0

        if self.max_row_count < self.row_counts[dest_root]:
            self.max_row_count = self.row_counts[dest_root]

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        # parents_to_update = []

        # Find root.
        # root = table
        # while root != self.parents[root]:
        #     parents_to_update.append(self.parents[root])
        #     root = self.parents[root]

        # # Compress path.
        # for i in parents_to_update:
        #     self.parents[i] = root
        if self.parents[table] != table:
            self.parents[table] = self.get_parent(self.parents[table]) 

        return self.parents[table]

def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(src-1, dst-1)
        print(db.max_row_count)

if __name__ == "__main__":
    main()