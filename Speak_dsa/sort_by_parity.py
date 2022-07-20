def sortArrayByParity(nums):
    evens = []
    odds = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
    print('evens= ', evens)
    print('odds= ', odds)
    return evens + odds

nums1 = [3,1,2,4]
test1 = sortArrayByParity(nums1)
print(test1)