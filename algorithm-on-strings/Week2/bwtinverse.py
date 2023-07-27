# python3
import sys



def InverseBWT(bwt):
    repetition_dict = {"A": 0, "C": 0, "G": 0, "T": 0, "$": 0}
    bwt_last_column = []
    for i in bwt:
        bwt_last_column.append(i + str(repetition_dict[i]))
        repetition_dict[i] += 1
    idx = 0
    make_str = ""
    for i in range(len(bwt) - 1):
        s = bwt_last_column[idx]
        make_str += s[0]
        if s[0] == "A":
            idx = repetition_dict["$"] + int(s[1:])
        elif s[0] == "C":
            idx = repetition_dict["$"] + repetition_dict["A"] + int(s[1:])
        elif s[0] == "G":
            idx = repetition_dict["$"] + repetition_dict["A"] + \
                repetition_dict["C"] + int(s[1:])
        elif s[0] == "T":
            idx = repetition_dict["$"] + repetition_dict["A"] + \
                repetition_dict["C"] + repetition_dict["G"] + int(s[1:])
    return make_str[::-1] + "$"





if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))