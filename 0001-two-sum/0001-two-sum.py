class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map = {}
    
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return(i, nums_map[target-n])
            nums_map[n] = i
            # 딕셔너리를 활용하여 nums[i] : index 로 설정하여 인덱스 중복을 방지한다.

        # My Solutuion
        # answer = []

        # for i, n in enumerate(nums):
        #     target_num = target - n
        #     if target_num in nums and i != nums.index(target_num):
        #         answer.append(i)
        #         answer.append(nums.index(target_num)) 
        #         break

        # return answer