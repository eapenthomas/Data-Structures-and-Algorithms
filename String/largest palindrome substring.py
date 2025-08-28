def longest_palindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        # Expand as long as the characters are equal and within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        return s[left +1:right]

    if not s:
        return ""

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome (single character center)
        odd_palindrome = expand_around_center(i, i)
        # Even length palindrome (two characters center)
        even_palindrome = expand_around_center(i, i + 1)

        # Update longest palindrome if needed
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest


# Example usage:
s = [1,2,4,5,6,7]
input_string = "abbacd"
print(longest_palindrome(input_string))  # Output: "bab" or "aba"
