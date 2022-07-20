def merge_sort(nums):
    #base case - empty list or list of single element
    if len(nums) <= 1:
        return nums

    mid = int(len(nums)/2)
    first_half = merge_sort(nums[0:mid])
    last_half = merge_sort(nums[mid:])
    return merge(first_half, last_half)

def merge(left, right):
    left_pointer = right_pointer = 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    # add what is left in either list
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

input1 = [1,5,3,2,8,7,6,4]
test1 = merge_sort(input1)
print(test1)