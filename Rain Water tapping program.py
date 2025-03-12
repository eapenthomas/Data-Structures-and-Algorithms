def trap(height):
    if not height:  # Check if the list is empty
        return 0
    f = 0  # Front pointer
    r = len(height) - 1  # Rear pointer
    w = 0  # Water trapped
    fm = height[f]  # Front maximum
    rm = height[r]  # Rear maximum

    while f < r:  # While front pointer is less than rear pointer
        if height[f] <= height[r]:  # If front height is less than or equal to rear height
            if height[f] >= fm:  # Update front maximum if current height is greater
                fm = height[f]
            else:  # Calculate trapped water
                w += fm - height[f]
            f += 1  # Move front pointer forward
        else:  # If rear height is less than front height
            if height[r] >= rm:  # Update rear maximum if current height is greater
                rm = height[r]
            else:  # Calculate trapped water
                w += rm - height[r]
            r -= 1  # Move rear pointer backward

    return w  # Return the total water trapped

# Example usage
height = [2,6,0,4]
print("Total units that can be stored = ",trap(height))  # Output: 6
