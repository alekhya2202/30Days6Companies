def encode(arr):
    # Code here
    out = "" + arr[0]
    char_cnt = 1
    for i in range(1, len(arr)):
        if arr[i] == out[-1]:
            char_cnt += 1
        else:
            out += str(char_cnt)
            out += arr[i]
            char_cnt = 1
    out += str(char_cnt)
    return out
