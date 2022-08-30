class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        if k < 0:
            return 0
        result, lookup = set(), set()
        for num in nums:
            if num-k in lookup:
                result.add(num-k)
                
            if num+k in lookup:
                result.add(num+k)
            lookup.add(num)
        print(lookup)
        print(result)
        return len(result)
      
      
m = Solution()


print(m.findPairs(nums=[3,1,6,1,9], k=2))