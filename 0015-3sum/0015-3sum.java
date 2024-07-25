import java.util.*;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        Arrays.sort(nums);

        List<List<Integer>> triplets = new ArrayList<List<Integer>>();
        int sum = 0;

        for(int i=0; i<nums.length-2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int left = i + 1;
            int right = nums.length-1;

            while(left < right) {
                sum = nums[i] + nums[left] + nums[right];

                if (sum < 0) { left++; }
                else if (sum > 0) { right--; }
                else {
                    // List에 배열을 초기값으로 삽입하기
                    List<Integer> triplet = Arrays.asList(nums[i], nums[left], nums[right]);
                    triplets.add(triplet);

                    while (left < right && nums[left] == nums[left+1]) { left++; }
                    while (left < right && nums[right] == nums[right-1]) { right--; }

                    left++;
                    right--;
                }
            }
        }

        return triplets;
        
    }
}