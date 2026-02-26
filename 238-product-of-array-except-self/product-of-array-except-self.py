class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = math.prod(nums)
        answer = []
        for i in range(len(nums)):
            if nums[i] != 0:
                answer.append(int(result / nums[i]))
            else: 
                answer.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
        return answer