# python3
import sys

def sort_doubled(s , L , order , classified):
    count = [0 for i in range(len(s))]
    neworder = [0 for i in range(len(s))]
    for i in range(len(s)):
        count[classified[i]] 


def build_suffix_array(text):
    result = []
    for i in range(0 , len(text)):
        result.append((text[i:] , i))
    result.sort(key = lambda x : x[0])
    return [i[1] for i in result]

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))