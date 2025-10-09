import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        int n = words.length;
        int i = 0; // Index to track current word position

        List<String> result = new ArrayList<>();

        // Process the words in groups that can fit on one line
        while (i < n) {
            int lineLength = words[i].length();
            int last = i + 1; // Track the position of the next word

            while (last < n && lineLength + 1 + words[last].length() <= maxWidth) {
                lineLength += 1 + words[last].length(); 
                last++;
            }

            StringBuilder sb = new StringBuilder(); 
            int wordCount = last - i;

            if (last == n || wordCount == 1) {
                for (int j = i; j < last; j++) {
                    sb.append(words[j]); // Append each word to the line
                    if (j < last - 1) sb.append(" "); // Add a single space between words
                }
                sb.append(" ".repeat(maxWidth - sb.length()));
            } else {
    
                int totalSpaces = maxWidth - lineLength + wordCount - 1; // Extra space to fill
                int spaceBetween = totalSpaces / (wordCount - 1); // Base number of spaces between words
                int extraSpaces = totalSpaces % (wordCount - 1); // Extra spaces to distribute evenly

                for (int j = i; j < last - 1; j++) {
                    sb.append(words[j]); // Append each word
                    // Add spaces: some words get an extra if extraSpaces > 0
                    sb.append(" ".repeat(spaceBetween + (extraSpaces-- > 0 ? 1 : 0)));
                }
                sb.append(words[last - 1]); // Add the last word in the line without extra space after it
            }

            result.add(sb.toString()); // Add the fully justified line to the result
            i = last; // Move to the next set of words
        }

        return result; // Return the list of justified lines
    }
}
