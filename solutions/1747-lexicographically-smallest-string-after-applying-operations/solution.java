import java.util.*;

public class Solution {
    public String findLexSmallestString(String s, int a, int b) {
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        String min = s;

        queue.offer(s);
        visited.add(s);

        while (!queue.isEmpty()) {
            String curr = queue.poll();
            if (curr.compareTo(min) < 0) {
                min = curr;
            }

            // Operation 1: Add 'a' to all odd indices
            char[] chars = curr.toCharArray();
            for (int i = 1; i < chars.length; i += 2) {
                chars[i] = (char) ((chars[i] - '0' + a) % 10 + '0');
            }
            String added = new String(chars);
            if (!visited.contains(added)) {
                visited.add(added);
                queue.offer(added);
            }

            // Operation 2: Rotate right by b positions
            String rotated = curr.substring(curr.length() - b) + curr.substring(0, curr.length() - b);
            if (!visited.contains(rotated)) {
                visited.add(rotated);
                queue.offer(rotated);
            }
        }

        return min;
    }
}
