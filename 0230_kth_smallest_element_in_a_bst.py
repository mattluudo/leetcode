"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

class Solution(object):
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # In-order tree treversal and append to list. Return the (k-1)th value in the list
    def kthSmallest_brute(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        """
        def sort (root):
            if root:
                sort(root.left)
                print(root.val)
                sort(root.right)
            else:
                print('NA')
        """
        
        asc_list = []
        def sort(root):
            if root:
                sort(root.left)
                asc_list.append(root.val)
                sort(root.right)
                
            else: 
                return 

        sort(root)
        return asc_list[k-1]
    
            
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Same with brute kthSmallest_brute solution, but exits the tree treversal when the list is length k
    def kthSmallest_fast(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        """
        def sort (root):
            if root:
                sort(root.left)
                print(root.val)
                sort(root.right)
            else:
                print('NA')
        """
        
        asc_list = []
        def sort(root):
            if root:
                if len(asc_list) < k:
                    sort(root.left)
                else: return
                
                if len(asc_list) < k:
                    asc_list.append(root.val)
                else: return
                
                if len(asc_list) < k:
                    sort(root.right)
                else: return
                
            else: 
                return 

        sort(root)
        return asc_list[-1]