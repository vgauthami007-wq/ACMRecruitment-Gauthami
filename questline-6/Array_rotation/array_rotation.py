def rotate(nums, k):
    n = len(nums)
    k = k % n  # normalize k
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original:", nums)
    rotate(nums, k)
    print("Rotated:", nums)
