"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution(object):
    
    # Converts to str and reverse with time O(log(x)) and space O(log(x) where x is the integer
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
            
        # Handle negative number inputs
        s = str(x)
        if s[0] == '-':
            is_neg = True
        else :
            is_neg = False
        s = s.lstrip('-')
        
        # Reverse string
        result = int(s[::-1])
        if is_neg:
            result = result * -1
        
        # Return 0 if integer overflows
        if result >= 2**31-1 or result <= -2**31: 
            return 0
        
        return result

