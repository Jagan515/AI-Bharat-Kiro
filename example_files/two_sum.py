"""
Two Sum Problem - Array problem using hash map
Given an array of integers, return indices of two numbers that add up to target.
"""

def two_sum(nums, target):
    """
    Find two numbers in array that sum to target.
    Uses hash map for O(n) time complexity.
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


if __name__ == "__main__":
    # Test cases
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices: {result}")  # Output: [0, 1]
    
    nums = [3, 2, 4]
    target = 6
    result = two_sum(nums, target)
    print(f"Indices: {result}")  # Output: [1, 2]
