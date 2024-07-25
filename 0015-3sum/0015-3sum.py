class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sum = 0
        triplets = []

        # 세수의 합이므로 끝까지 순회X -> 맨뒤에 2개는 조회할 필요X -> 뒤에서 3번째를 기준으로 합=0이 없다면 답이 없는것.
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            left, right = i + 1, len(nums) - 1 

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else: # sum = 0 answer triplet
                    triplets.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                    
        return triplets
         