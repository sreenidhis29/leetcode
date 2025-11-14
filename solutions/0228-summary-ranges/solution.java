import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        if (nums.length == 0) {
            return result;
        }

        int start = nums[0];

        for (int i = 1; i <= nums.length; i++) {
            // Check for end of range or end of array
            if (i == nums.length || nums[i] != nums[i - 1] + 1) {
                if (start == nums[i - 1]) {
                    result.add(String.valueOf(start)); // Single number
                } else {
                    result.add(start + "->" + nums[i - 1]); // Range
                }
                if (i < nums.length) {
                    start = nums[i];
                }
            }
        }

        return result;
    }
}
