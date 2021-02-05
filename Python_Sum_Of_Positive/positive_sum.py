def positive_sum(arr):
    count = 0
    for num in arr:
        if num >= 0:
            count += num
    return count