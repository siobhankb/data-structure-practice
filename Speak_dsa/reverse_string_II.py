# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg" <-- switched ab>ba AND ef>fe
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"


def swapSlice(s_slice):
    slice_lst = list(s_slice)
    beg = 0
    length = len(slice_lst)
    end = length - 1
    if end == beg:
        return s_slice
    elif end == 1:
        slice_lst[beg], slice_lst[end] = slice_lst[end], slice_lst[beg]
        return ''.join(slice_lst)
    else:            
        mid = length // 2
        while beg < mid:
            slice_lst[beg], slice_lst[end] = slice_lst[end], slice_lst[beg]
            beg += 1
            end -= 1
        return ''.join(slice_lst)

def reverseStrToK(s, k):
    s_length = len(s)
    if s_length == 1:
        return s
    beg = 0
    s_end = s_length - 1
    step = k * 2
    end = step
    output = ''
    while end <= s_end:
        s_slice = s[beg:end]
        skip_slice = s_slice[k:k*2]
        rev_slice = swapSlice(s_slice[:k])
        output += rev_slice + skip_slice
        beg += step
        end += step
    check_end = len(output)
    if check_end < s_length:
        s_slice = s[check_end:]
        check_length = len(s_slice)
        if check_length <= k:
            rev_slice = swapSlice(s_slice)
            output += rev_slice
        else:
            rev_slice = swapSlice(s_slice[:k])
            skip_slice = s_slice[k:]
            output += rev_slice + skip_slice
    return output


s1 = "abcdefg"
k1 = 2

s2 = "abcd"
k2 = 2

s3 = "abcdefghi"
k3 = 3

s4 = "abcdefgh"
k4 = 3

s5 = "abcd"
k5 = 4

s6 = "a"
k6 = 1

s7 = "abcdefg"
k7 = 1

# test1 = reverseStrToK(s1, k1)
# print(test1)

# test2 = reverseStrToK(s2, k2)
# print(test2)

# test3 = reverseStrToK(s3, k3)
# print(test3)

# test4 = reverseStrToK(s4, k4)
# print(test4)

# test5 = reverseStrToK(s5, k5)
# print(test5)

# test6 = reverseStrToK(s6, k6)
# print(test6)

test7 = reverseStrToK(s7, k7)
print(test7)