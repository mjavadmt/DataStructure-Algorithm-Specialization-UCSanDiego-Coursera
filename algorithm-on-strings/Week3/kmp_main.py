# python3
import sys

def compute_prefix_function(p):
    s = [0]
    border = 0 
    for i in range(1,len(p)):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s.append(border)
    return s 


def find_pattern(pattern, text):
    if len(pattern) > len(text):
        return []
    result = []
    make_str = pattern + "$" + text
    prefix_array = compute_prefix_function(make_str)
    for i in range(len(pattern) + 1 , len(make_str)):
        if prefix_array[i] == len(pattern):
            result.append(i - 2*len(pattern))
    return result


if __name__  == "__main__":
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))