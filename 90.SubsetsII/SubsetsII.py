class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets if s + [n] not in subsets]
            
        return subsets