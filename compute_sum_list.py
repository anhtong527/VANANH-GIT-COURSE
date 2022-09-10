def sum_list(nums):
    if not all([isinstance(num, int) for num in nums]):
        raise ValueError('the list contains non-number.')
    return sum(nums)