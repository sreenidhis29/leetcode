import java.util.HashMap;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");

        if (pattern.length() != words.length) return false;

        Map<Character, String> patternToWord = new HashMap<>();
        Map<String, Character> wordToPattern = new HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String word = words[i];

            if (patternToWord.containsKey(c)) {
                if (!patternToWord.get(c).equals(word)) {
                    return false;
                }
            } else {
                patternToWord.put(c, word);
            }

            if (wordToPattern.containsKey(word)) {
                if (wordToPattern.get(word) != c) {
                    return false;
                }
            } else {
                wordToPattern.put(word, c);
            }
        }

        return true;
    }
}
