
Input:  
nums = [1,2,3,4,5,6,7], k = 3  
Output:  
[5,6,7,1,2,3,4]



We need to move each element to a new position that is shifted `k` steps to the right.  
If `k` is larger than the array length `n`, then rotating by `k` is the same as rotating by `k % n`.

# Method:
1. Normalize `k` by `k = k % n`.
2. Reverse the whole array.
3. Reverse the first `k` elements.
4. Reverse the remaining `n-k` elements.

This uses O(1) extra space and O(n) time.
