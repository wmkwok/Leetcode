# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = ["" for x in range(numRows)]
        count = 0
        start = 0
        end = numRows
        inc = 1

        # while we dont run out of letters
        while count < len(s):
            # count from index 0 -> numRows
            for i in range(start, end, inc):
                if count < len(s):
                    rows[i] += s[count]
                    count += 1

            if inc == 1:
                inc = -1
                start = numRows-2
                end = 0
            else:
                inc = 1
                start = 0
                end = numRows
        print rows
        return "".join(rows)
            

sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
sol.convert(s, numRows)
