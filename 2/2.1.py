
def minimum(arr):
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
        else:
            continue
    return min 


def maximum(arr):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
        else:
            continue
    return max

info = input('Enter integers using "," to split: ')
nums = info.split(',')
for i in nums:
    i = int(i)


print(f'Minimum: {minimum(nums)}')
print(f'Maximum: {maximum(nums)}')