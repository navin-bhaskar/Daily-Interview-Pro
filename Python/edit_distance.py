"""                 Shree Krishnaya Namaha          """

class Solution(object):
    """Finding the edit distance between two strings https://leetcode.com/problems/edit-distance/"""
    def minDistance(self, word1, word2):
        shorter, longer = (word1, word2) if len(word1) < len(word2) else (word2, word1)
        edit_wks = [[col for col in range(len(shorter)+1)] for row in range(2)]

        for row in range(1, len(longer)+1):
            edit_wks[1][0] = row
            for col in range(1, len(shorter)+1):
                if shorter[col-1] == longer[row-1]:
                    edit_wks[1][col] = edit_wks[0][col-1]
                else:
                    edit_wks[1][col] = 1 + min(edit_wks[0][col-1], edit_wks[0][col],
                                                edit_wks[1][col-1])
            edit_wks[0], edit_wks[1] = edit_wks[1], edit_wks[0]

        return edit_wks[0][-1]

if __name__ == "__main__":
    sol = Solution()
    print (sol.minDistance("horse", "ros"))    
