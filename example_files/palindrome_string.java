/**
 * Check if a string is a palindrome
 * String manipulation problem
 */
public class PalindromeString {
    
    // Method 1: Using two pointers
    public static boolean isPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }
        
        // Convert to lowercase and remove non-alphanumeric
        s = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    // Method 2: Using string reversal
    public static boolean isPalindromeReverse(String s) {
        s = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        String reversed = new StringBuilder(s).reverse().toString();
        return s.equals(reversed);
    }
    
    public static void main(String[] args) {
        String test1 = "A man, a plan, a canal: Panama";
        String test2 = "race a car";
        
        System.out.println("'" + test1 + "' is palindrome: " + isPalindrome(test1));
        System.out.println("'" + test2 + "' is palindrome: " + isPalindrome(test2));
    }
}
