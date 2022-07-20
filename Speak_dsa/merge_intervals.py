# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# # NAIVE SOLUTION (doesn't work in all cases anyway)
# def mergeIntervals(interval_list):
#     sorted_list = sorted(interval_list)
#     checkMap = {
#         'a': sorted_list[0][0],
#         'z': sorted_list[0][1]
#     }
#     check_list = sorted_list[1:]
#     output = []
#     for i in range(1, len(interval_list)):
#         check = check_list.pop(0)
#         a = check[0]
#         z = check[1]
#         print('checkMap is: ', checkMap)
#         print('cheking a= ', a, ' and z= ', z)
#         if a >= checkMap['a'] and z <= checkMap['z']:
#             # this interval is contained already - skip & delete
#             pass
#         elif a <= checkMap['a'] and z >= checkMap['z']:
#             # this interval contains original - replace & delete original
#             checkMap['a'] = a
#             checkMap['z'] = z
#         elif z < checkMap['a'] or a > checkMap['z']:
#             # if interval ends before or starts after, 
#             # add to output
#             output.append(check)
#         elif a <= checkMap['a'] and z <= checkMap['z']:
#             # if interval starts before, but ends within
#             # reset beg
#             checkMap['a'] = a
#         elif a >= checkMap['a'] and z >= checkMap['z']:
#             # if interval starts within, but ends after,
#             # reset end
#             checkMap['z'] = z
#     output.append([checkMap['a'], checkMap['z']])
#     return output


# Better solution
def mergeIntervals(interval_list):
    interval_list.sort()
    print('sorted list= ', interval_list)
    merge = [interval_list[0]]
    for i in range(1, len(interval_list)):
        # overlaps if i starts before merge ends
        check = interval_list[i]
        print('check = ', check)
        print('merge[-1][1] = ', merge[-1][1])
        # if overlap, but not contained
        if check[0] <= merge[-1][1] and check[1] >= merge[-1][1]:
            # reset end value of current interval
            merge[-1][1] = check[1]
        # if it doesn't overlap, it must be greater bc list is sorted
        elif check[0] > merge[-1][1]:
            # so just append to output
            merge.append(check)
    return merge


# int1 = [[1,4],[4,5]]
# # Output: [[1,5]]
# test1 = mergeIntervals(int1)
# print('test1= ', test1)

# int2 = [[1,3],[2,6],[8,10],[15,18]]
# # Output: [[1,6],[8,10],[15,18]]
# test2 = mergeIntervals(int2)
# print('test2= ', test2)

# int3 = [[4,5],[1,4],[0,1]]
# # Output: [[0,5]]
# test3 = mergeIntervals(int3)
# print('test3= ', test3)

int4 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
# Output: [[1,10]]
test4 = mergeIntervals(int4)
print('test4= ', test4)

int5 = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
# Output: [[1,3],[4,7]]
test5 = mergeIntervals(int5)
print('test5= ', test5)