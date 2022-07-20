def reverseStr(s):
    beg = 0
    end = -1
    length = len(s)
    mid = len(s) // 2
    while beg < mid:
        s[beg], s[end] = s[end], s[beg]
        beg += 1
        end -= 1