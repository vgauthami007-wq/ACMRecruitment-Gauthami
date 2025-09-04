def rotate(nums, k):
    n = len(nums)
    k = k % n  # normalize k
    
    # helper function to reverse part of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # step 1: reverse whole array
    reverse(0, n - 1)
    # step 2: reverse first k elements
    reverse(0, k - 1)
    # step 3: reverse remaining elements
    reverse(k, n - 1)

# ---- Test the function ----
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original:", nums)
    rotate(nums, k)
    print("Rotated:", nums)
