class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            current_length = 1
            current_num = num
            if num - 1 in nums_set:
                continue
            
            while current_num + 1 in nums_set:
                current_length += 1
                current_num += 1
            
            longest = max(longest, current_length)

        return longest