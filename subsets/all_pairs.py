# use "subsets" algo pattern
def allPairs(lst):
    length = len(lst)
    pairs = []
    n = 0
    while n <= length - 1:
        for i in range(n + 1, length):
            pairs.append((n, i))
        n += 1
    return pairs