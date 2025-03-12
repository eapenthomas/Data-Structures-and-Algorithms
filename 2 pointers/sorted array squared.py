def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i, j = 0, len(nums) - 1

    result = []  # Separate list to store the sorted squares

    while i <= j:
        left_square = nums[i] ** 2
        right_square = nums[j] ** 2
        if left_square >  right_square:
            result.append(left_square)
            i += 1
        else:
            result.append(right_square)
            j -= 1

    return result[::-1]  # Return the separate result list

# Test cases
print(sortedSquares([-7,-3,2,3,11]))   # [1, 4, 9, 16, 25, 36]
print(sortedSquares([-7, -2, 3, 4, 5, 6])) # [4, 9, 9, 16, 25, 49]
