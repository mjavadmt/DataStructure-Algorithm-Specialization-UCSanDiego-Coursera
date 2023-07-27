# python3

def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(s, x, prime):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans


def precompute_hashes(text, length_pattern, big_prime, x):
    list_array = [0 for i in range(len(text) - length_pattern + 1)]
    last_text = text[-length_pattern:]
    list_array[-1] = poly_hash(last_text, x, big_prime)
    y = 1
    for i in range(1, length_pattern + 1):
        y = (y * x) % big_prime
    for i in range(len(text) - length_pattern - 1, -1, -1):
        list_array[i] = (x * list_array[i + 1] + ord(text[i]) - y * ord(text[i + length_pattern])) % big_prime
    return list_array


def get_occurrences(pattern, text):
    _multiplier = 263
    _prime = 1000000007
    positions = []
    text_hashes = precompute_hashes(text, len(pattern), _prime, _multiplier)
    pattern_hash = poly_hash(pattern, _multiplier, _prime)
    for i in range(len(text) - len(pattern) + 1):
        if text_hashes[i] == pattern_hash:
            if text[i:i + len(pattern)] == pattern:
                positions.append(i)
    return positions


# get_occurrences("aba", "abacaba")

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
