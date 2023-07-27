# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for q in queries:
        if q.type == "add":
            contacts[q.number] = q.name
        elif q.type == "del":
            try:
                del contacts[q.number]
            except KeyError:
                pass
        elif q.type == "find":
            try:
                check_item = contacts[q.number]
            except KeyError:
                check_item = "not found"
            result.append(check_item)

    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
