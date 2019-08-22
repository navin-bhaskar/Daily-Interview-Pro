class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        sub_solution = [[None for _ in range(len(s))] for _ in range(len(s))]

        # The sub solution matrix represents solution for each of the substring within the main string
        # matrix(i, j) indicates wether the string s[i:j+1] is a palindrome or not
        # Single char is a palindrome by definiation hence all diagonal elements must (i==j) must be true
        for i in range(0, len(s)):
            sub_solution[i][i] = True

        longest_pal_sub = s[0]
        # Now, check if two characters between i, i+1 are palindrome or not
        for i in range(0, len(s)-1):
            if s[i] == s[i + 1]:
                longest_pal_sub = s[i:i+2]
                sub_solution[i][i + 1] = True
        
        # Now we have a matrix that has solution for substrings with two characters
        # Using this, we can evaluate if a string a i, j is a substring if 
        # sub_solution[i+1][j-1] is a palindrome and s[i] is same as s[j] 
        # By doing this we are making use of the smaller problem that we had already solved 

        # We will consider only the matirx elements upper right of the matrix diagonal
        row_idx = 0
        col_idx = 3
        

        while col_idx <= len(s):         # Visit all the elements in the column
            while row_idx < (len(s) - col_idx + 1): # Visit only upper half
                i = row_idx
                j = row_idx + col_idx - 1
                sub_solution[i][j] = sub_solution[i+1][j-1] and s[i] == s[j]
                if sub_solution[i][j]:
                    longest_pal_sub = s[i:j+1]
                row_idx += 1
            row_idx = 0
            col_idx += 1

        return longest_pal_sub