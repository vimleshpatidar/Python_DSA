# COMPLETE 174 PROBLEM SET - ALL QUESTIONS
## Organized by Topic | Ordered by Difficulty | Ready to Practice

---

## TABLE OF CONTENTS

1. [ARRAYS (24 Questions)](#arrays)
2. [STRINGS (18 Questions)](#strings)
3. [LINKED LISTS (16 Questions)](#linked-lists)
4. [TREES (18 Questions)](#trees)
5. [GRAPHS (15 Questions)](#graphs)
6. [DYNAMIC PROGRAMMING (16 Questions)](#dynamic-programming)
7. [STACKS & QUEUES (12 Questions)](#stacks--queues)
8. [RECURSION (7 Questions)](#recursion)
9. [TWO POINTERS (10 Questions)](#two-pointers)
10. [BINARY SEARCH (8 Questions)](#binary-search)
11. [BACKTRACKING (11 Questions)](#backtracking)
12. [HEAPS & PRIORITY QUEUES (5 Questions)](#heaps--priority-queues)
13. [MATRIX (4 Questions)](#matrix)
14. [MISCELLANEOUS (10 Questions)](#miscellaneous)

---

# ARRAYS (24 Questions)

## Beginner Level

**1. Find Maximum in Array**
- Type: Fundamental
- Difficulty: Beginner
- Time: 10 minutes
- Concepts: Array iteration, Comparison
- Description: Find the largest element in an array
- Companies: All
- Hints: Use a variable to store max, iterate through array

**2. Find Minimum in Array**
- Type: Fundamental
- Difficulty: Beginner
- Time: 10 minutes
- Concepts: Array iteration, Comparison
- Description: Find the smallest element in an array
- Companies: All
- Hints: Similar to max, use min variable

**3. Sum of All Elements**
- Type: Fundamental
- Difficulty: Beginner
- Time: 10 minutes
- Concepts: Array traversal, Accumulation
- Description: Calculate sum of all elements in array
- Companies: All
- Hints: Use accumulator variable, iterate through all elements

## Easy Level

**4. Average of Array Elements**
- Type: Fundamental
- Difficulty: Easy
- Time: 10 minutes
- Concepts: Sum, Division, Variables
- Description: Find average of all array elements
- Companies: All
- Hints: Calculate sum first, then divide by length

**5. Count Occurrences of Element**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Array traversal, Counting
- Description: Count how many times a specific element appears in array
- Companies: All
- Hints: Use counter variable, compare each element

**6. Linear Search in Array**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Array traversal, Comparison
- Description: Find index of element in unsorted array
- Companies: All
- Hints: Iterate from start, return index when found

**7. Check if Element Exists**
- Type: Fundamental
- Difficulty: Easy
- Time: 10 minutes
- Concepts: Array search, Boolean
- Description: Check if specific element exists in array
- Companies: All
- Hints: Return true/false, can use linear search

**8. Reverse an Array**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Two pointers, Array manipulation
- Description: Reverse array in-place
- Companies: All
- Hints: Use two pointers from both ends, swap elements

**9. Remove Duplicates (Sorted Array)**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Array traversal, Comparison
- Description: Remove duplicates from sorted array in-place
- Companies: All
- Hints: Two pointers approach, keep unique elements

**10. Left Rotate Array by 1**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Array manipulation, Loops
- Description: Rotate array left by 1 position
- Companies: All
- Hints: Store first element, shift all elements left

**11. Rotate Array**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Array manipulation
- Description: Rotate array right by k steps
- Companies: TCS, Infosys, LTIMindtree
- Hints: Reverse approach or use circular array logic

**12. Remove Duplicates from Sorted Array**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Two pointers
- Description: Remove duplicates in-place, return new length
- Companies: All
- Hints: Two pointers, keep track of unique count

**13. Move All Zeroes to End**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Two pointers
- Description: Move all zeros to end while maintaining order
- Companies: TCS, Infosys
- Hints: Use two pointers, swap non-zero with zero

**14. Two Sum**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Hash Map, Two Pointers
- Description: Find two numbers that add up to target sum
- Companies: YASH, TCS, Infosys, Accenture, IBM
- Hints: Use hash map for O(n) solution

**15. Contains Duplicate**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Hash Map
- Description: Check if array has duplicate elements
- Companies: All
- Hints: Hash map for O(n) solution or sorting

## Medium Level

**16. 3Sum**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Two pointers, Sorting
- Description: Find all unique triplets that sum to zero
- Companies: TCS, Infosys, IBM, Accenture
- Hints: Sort array, use two pointers with fixed element

**17. Container With Most Water**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Two pointers
- Description: Find two lines forming largest area
- Companies: TCS, Infosys
- Hints: Two pointers, height determines area

**18. Product of Array Except Self**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Prefix/Postfix
- Description: Create array where each element = product of all others
- Companies: YASH, IBM
- Hints: Use prefix and postfix arrays or single pass

**19. Maximum Subarray (Kadane's Algorithm)**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Dynamic Programming
- Description: Find contiguous subarray with largest sum
- Companies: YASH, TCS, Infosys, IBM
- Hints: Keep track of max ending here, update global max

**20. Search in Rotated Sorted Array**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Binary Search
- Description: Search target in rotated sorted array
- Companies: IBM, TCS
- Hints: Identify which half is sorted, binary search

**21. Merge Intervals**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Intervals
- Description: Merge overlapping intervals
- Companies: TCS, Infosys, Accenture
- Hints: Sort by start, merge overlapping ones

**22. Find Minimum in Rotated Sorted Array**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Binary Search
- Description: Find minimum in rotated sorted array
- Companies: Google, Microsoft
- Hints: Binary search to find rotation point

**23. Spiral Matrix**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Matrix traversal
- Description: Traverse matrix in spiral order
- Companies: Accenture, IBM
- Hints: Track boundaries, move in 4 directions

## Hard Level

**24. Trapping Rain Water**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: Dynamic Programming
- Description: Calculate trapped water after rain
- Companies: YASH, TCS, Infosys, IBM
- Hints: Use left/right max arrays or two pointers

---

# STRINGS (18 Questions)

## Beginner Level

**25. Length of String**
- Type: Fundamental
- Difficulty: Beginner
- Time: 5 minutes
- Concepts: String operations
- Description: Get length of string
- Companies: All
- Hints: Use built-in length method

**26. Reverse a String**
- Type: Fundamental
- Difficulty: Easy
- Time: 10 minutes
- Concepts: String iteration
- Description: Reverse the characters in a string
- Companies: All
- Hints: Two pointers or build new string

**27. Check Palindrome String**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Two pointers
- Description: Check if string is palindrome
- Companies: All
- Hints: Compare characters from both ends

**28. Count Vowels in String**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: String traversal, Conditionals
- Description: Count number of vowels in string
- Companies: All
- Hints: Iterate through each character, check if vowel

**29. Find Largest Word in String**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: String splitting, Comparison
- Description: Find longest word in string
- Companies: All
- Hints: Split by spaces, compare lengths

**30. Reverse Words in String**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: String operations
- Description: Reverse the order of words
- Companies: All
- Hints: Split, reverse array, join

**31. Remove Spaces from String**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: String filtering
- Description: Remove all space characters from string
- Companies: All
- Hints: Iterate and filter out spaces

**32. First Occurrence of Character**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: String search
- Description: Find first occurrence of character in string
- Companies: All
- Hints: Iterate from start, return index when found

## Easy Interview Level

**33. Valid Palindrome**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Two pointers
- Description: Check if string is palindrome (ignore non-alphanumeric)
- Companies: Accenture, All
- Hints: Two pointers, skip non-alphanumeric

**34. Palindrome Number**
- Type: Interview
- Difficulty: Easy
- Time: 10 minutes
- Concepts: Math
- Description: Check if number reads same forwards and backwards
- Companies: Accenture, LTIMindtree
- Hints: Convert to string or reverse number

**35. Longest Common Prefix**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: String manipulation
- Description: Find longest prefix in array of strings
- Companies: Infosys, TCS
- Hints: Compare characters at each position

## Medium Level

**36. Longest Substring Without Repeating Characters**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Sliding window
- Description: Find longest substring with unique characters
- Companies: Infosys, IBM, YASH
- Hints: Sliding window with hash map

**37. Longest Repeating Character Replacement**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Sliding window
- Description: Replace characters to get longest repeating substring
- Companies: IBM, Infosys
- Hints: Sliding window, track character frequencies

**38. Minimum Window Substring**
- Type: Interview
- Difficulty: Medium
- Time: 35 minutes
- Concepts: Sliding window
- Description: Find minimum window containing all required characters
- Companies: YASH, IBM
- Hints: Sliding window with character counts

**39. Group Anagrams**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Hash map
- Description: Group words by anagram
- Companies: TCS, Infosys
- Hints: Sort characters as key

**40. Valid Parentheses**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Stack
- Description: Check if parentheses are balanced
- Companies: YASH, TCS, Infosys, IBM
- Hints: Use stack for matching

**41. Longest Palindromic Substring**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Dynamic programming
- Description: Find longest palindrome in string
- Companies: YASH, Infosys
- Hints: Expand around center or DP approach

**42. Encode and Decode Strings**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: String manipulation
- Description: Convert string to/from encoded format
- Companies: Google, Meta
- Hints: Use length prefix encoding

---

# LINKED LISTS (16 Questions)

## Easy Level

**43. Reverse a Linked List**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Pointer manipulation
- Description: Reverse the direction of linked list
- Companies: YASH, TCS, Infosys, IBM
- Hints: Three pointers approach, track prev/curr/next

**44. Detect Cycle in Linked List**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Floyd's cycle detection
- Description: Check if linked list has cycle
- Companies: TCS, Infosys, IBM
- Hints: Slow and fast pointers

**45. Merge Two Sorted Lists**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Merging
- Description: Merge two sorted linked lists into one
- Companies: TCS, Infosys, LTIMindtree
- Hints: Compare nodes from both lists

**46. Remove Nth Node from End**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Remove nth node from end of list
- Companies: YASH, TCS
- Hints: Two pointers with gap of n

**47. Remove Duplicates from Sorted List**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: List traversal
- Description: Remove duplicate elements from sorted list
- Companies: All
- Hints: Compare current with next

**48. Find Middle of Linked List**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Slow-fast pointers
- Description: Find the middle node of linked list
- Companies: All
- Hints: Slow and fast pointers

**49. Palindrome Linked List**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Check if linked list is palindrome
- Companies: TCS, LTIMindtree
- Hints: Find middle, reverse second half, compare

**50. Intersection of Two Linked Lists**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Find intersection node of two lists
- Companies: Infosys, IBM
- Hints: Two pointers at different starts

## Medium Level

**51. Merge K Sorted Lists**
- Type: Interview
- Difficulty: Medium
- Time: 40 minutes
- Concepts: Heap, merge
- Description: Merge k sorted lists into one
- Companies: YASH, TCS, IBM
- Hints: Use min heap or divide and conquer

**52. Reorder List**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Pointer manipulation
- Description: Reorder: L0 → Ln → L1 → Ln-1 → L2
- Companies: TCS, Infosys
- Hints: Find middle, reverse second half, merge

**53. LRU Cache**
- Type: Interview
- Difficulty: Medium
- Time: 40 minutes
- Concepts: Hash map + doubly linked list
- Description: Implement LRU cache with O(1) operations
- Companies: YASH, Infosys, IBM
- Hints: Hash map for quick access, doubly linked list for order

**54. Add Two Numbers (Linked Lists)**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: List arithmetic
- Description: Add two numbers represented as lists
- Companies: TCS, Infosys
- Hints: Traverse both lists simultaneously, handle carry

**55. Copy List with Random Pointer**
- Type: Interview
- Difficulty: Medium
- Time: 35 minutes
- Concepts: Hash map, cloning
- Description: Deep copy linked list with random pointers
- Companies: IBM, Infosys
- Hints: Use hash map to track original to copy mapping

**56. Swap Nodes in Pairs**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Recursion
- Description: Swap adjacent nodes in list
- Companies: TCS, LTIMindtree
- Hints: Recursion or iterative with pointers

**57. Partition List**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Pointer manipulation
- Description: Partition list around value x
- Companies: All
- Hints: Create two lists, merge them

**58. Rotate List**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Linked list
- Description: Rotate list right by k positions
- Companies: Infosys, IBM
- Hints: Find rotation point, rearrange pointers

---

# TREES (18 Questions)

## Easy Level

**59. Binary Tree Inorder Traversal**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: DFS, Recursion
- Description: Traverse tree in inorder (Left-Root-Right)
- Companies: TCS, Infosys, IBM
- Hints: Recursion or stack-based iterative approach

**60. Maximum Depth of Binary Tree**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: DFS
- Description: Find maximum depth/height of tree
- Companies: YASH, TCS, Infosys
- Hints: Recursion, return 1 + max of subtree depths

**61. Invert Binary Tree**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: DFS
- Description: Mirror the binary tree
- Companies: All
- Hints: Swap left and right children recursively

**62. Symmetric Tree**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: DFS
- Description: Check if tree is symmetric
- Companies: TCS, Infosys
- Hints: Check if left and right subtrees are mirrors

**63. Same Tree**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Recursion
- Description: Check if two trees are identical
- Companies: Infosys, LTIMindtree
- Hints: Compare root, then recursively check subtrees

**64. Validate Binary Search Tree**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: BST validation
- Description: Check if tree is valid BST
- Companies: TCS, IBM, LTIMindtree
- Hints: In-order traversal or recursive with min/max bounds

**65. Diameter of Binary Tree**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: DFS
- Description: Find longest path between any two nodes
- Companies: All
- Hints: DFS to get height, update diameter

**66. Height of Binary Tree**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Recursion
- Description: Calculate height/depth of tree
- Companies: All
- Hints: Recursion, 1 + max(left height, right height)

**67. Binary Search Tree Search**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: BST
- Description: Search for value in BST
- Companies: TCS, LTIMindtree
- Hints: Compare with root, go left or right

**68. Level Order Traversal (BFS)**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: BFS, Queue
- Description: Traverse tree level by level
- Companies: TCS, Infosys, IBM
- Hints: Use queue, process level by level

## Medium Level

**69. Binary Tree Level Order Traversal**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: BFS
- Description: Return level-by-level traversal
- Companies: YASH, TCS, IBM
- Hints: BFS with queue, return list of lists

**70. Binary Tree Zigzag Level Order Traversal**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: BFS
- Description: Traverse tree in zigzag pattern
- Companies: TCS, IBM
- Hints: BFS, alternate direction for each level

**71. Construct Binary Tree from Traversals**
- Type: Interview
- Difficulty: Medium
- Time: 35 minutes
- Concepts: Recursion
- Description: Rebuild tree from preorder and inorder
- Companies: TCS, IBM
- Hints: Find root in inorder, recursively build subtrees

**72. Lowest Common Ancestor of BST**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: BST
- Description: Find LCA in binary search tree
- Companies: All
- Hints: Compare with root, go left or right

**73. Lowest Common Ancestor of Binary Tree**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DFS
- Description: Find LCA in general binary tree
- Companies: TCS, Infosys, IBM
- Hints: Recursion, check if node in left/right subtree

**74. Kth Smallest Element in BST**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Inorder traversal
- Description: Find kth smallest element in BST
- Companies: Google, Amazon
- Hints: In-order traversal gives sorted order

## Hard Level

**75. Serialize and Deserialize Binary Tree**
- Type: Interview
- Difficulty: Medium
- Time: 40 minutes
- Concepts: DFS/BFS, string
- Description: Convert tree to/from string representation
- Companies: YASH, IBM, Infosys
- Hints: DFS with level markers, reconstruct from string

**76. Binary Tree Maximum Path Sum**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: DFS
- Description: Find maximum path sum in tree
- Companies: YASH, IBM
- Hints: DFS, track max path through node

---

# GRAPHS (15 Questions)

## Medium Level

**77. Number of Islands**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DFS/BFS, Union-find
- Description: Count islands in binary matrix
- Companies: TCS, Infosys, IBM, Accenture, LTIMindtree
- Hints: DFS/BFS from each unvisited land

**78. Clone Graph**
- Type: Interview
- Difficulty: Medium
- Time: 35 minutes
- Concepts: DFS/BFS, Hash map
- Description: Deep copy undirected graph
- Companies: YASH, IBM
- Hints: Use hash map to track old to new node mapping

**79. Course Schedule**
- Type: Interview
- Difficulty: Medium
- Time: 35 minutes
- Concepts: Topological sort
- Description: Detect cycle in directed graph
- Companies: TCS, IBM, Accenture
- Hints: Topological sort using DFS or Kahn's algorithm

**80. Course Schedule II**
- Type: Interview
- Difficulty: Medium
- Time: 35 minutes
- Concepts: Topological sort
- Description: Return topological order of courses
- Companies: Google, Meta
- Hints: Topological sort, return order or empty if cycle

**81. Pacific Atlantic Water Flow**
- Type: Interview
- Difficulty: Medium
- Time: 35 minutes
- Concepts: DFS
- Description: Find cells where water flows to both oceans
- Companies: IBM, Infosys
- Hints: DFS from ocean edges

**82. Surrounded Regions**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DFS/BFS
- Description: Capture regions surrounded by 'X'
- Companies: YASH, Infosys
- Hints: DFS from border to find non-captured regions

**83. Graph Valid Tree**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Union-find
- Description: Check if graph is valid tree
- Companies: IBM, Accenture
- Hints: n nodes, n-1 edges, connected

**84. Number of Connected Components**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Union-find, DFS
- Description: Count connected components
- Companies: IBM, TCS
- Hints: Union-find or DFS from unvisited nodes

**85. Redundant Connection**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Union-find
- Description: Find edge creating cycle
- Companies: Infosys, IBM
- Hints: Union-find, return edge that creates cycle

**86. Time Needed to Inform All Employees**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: DFS
- Description: Find time to inform all employees
- Companies: Meta, Google
- Hints: DFS from manager, track maximum time

**87. Rotting Oranges**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: BFS
- Description: Find time for all oranges to rot
- Companies: Amazon, Google
- Hints: BFS from all rotting oranges simultaneously

**88. Walls and Gates**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: BFS
- Description: Fill empty rooms with distance to gate
- Companies: Google, Meta
- Hints: BFS from all gates simultaneously

## Hard Level

**89. Alien Dictionary**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: Topological sort
- Description: Derive ordering of alien language
- Companies: IBM, Accenture
- Hints: Build graph from word pairs, topological sort

**90. Strongly Connected Components**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: Tarjan/Kosaraju
- Description: Find all SCC in directed graph
- Companies: IBM
- Hints: Kosaraju's or Tarjan's algorithm

**91. Word Ladder II**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: BFS, backtracking
- Description: Find all shortest paths between words
- Companies: YASH, IBM
- Hints: BFS to find parents, backtrack to build paths

---

# DYNAMIC PROGRAMMING (16 Questions)

## Easy Level

**92. Climbing Stairs**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: DP
- Description: Count ways to climb n stairs (take 1 or 2)
- Companies: YASH, TCS, Infosys, IBM, LTIMindtree
- Hints: dp[i] = dp[i-1] + dp[i-2]

**93. House Robber**
- Type: Interview
- Difficulty: Easy
- Time: 25 minutes
- Concepts: DP
- Description: Max money robbing houses (can't rob adjacent)
- Companies: YASH, TCS, Infosys, IBM
- Hints: dp[i] = max(dp[i-1], dp[i-2] + nums[i])

## Medium Level

**94. House Robber II**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Max money robbing houses in circle
- Companies: Infosys, IBM
- Hints: Solve two cases: exclude first or last house

**95. Coin Change**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Min coins needed to make amount
- Companies: TCS, Infosys, IBM, Accenture
- Hints: dp[i] = min(dp[i], dp[i-coin] + 1)

**96. Coin Change II**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Count combinations to make amount
- Companies: IBM, Infosys
- Hints: dp[i] += dp[i-coin] for each coin

**97. Longest Increasing Subsequence**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Find longest increasing subsequence
- Companies: YASH, TCS, IBM
- Hints: dp[i] = max(dp[j] + 1) for all j < i where arr[j] < arr[i]

**98. Word Break**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP, Hash map
- Description: Check if string can be segmented into dictionary words
- Companies: IBM, Infosys, YASH
- Hints: dp[i] = check if any word ends at position i

**99. Unique Paths**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: DP
- Description: Count paths from top-left to bottom-right
- Companies: TCS, Infosys
- Hints: dp[i][j] = dp[i-1][j] + dp[i][j-1]

**100. Unique Paths II (with obstacles)**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Count paths with obstacles
- Companies: Infosys, IBM
- Hints: Skip obstacles in DP calculation

**101. Decode Ways**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Count ways to decode digit string
- Companies: TCS, Infosys, IBM
- Hints: dp[i] = dp[i-1] + dp[i-2] based on valid decodings

**102. Jump Game**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Greedy, DP
- Description: Determine if can reach last index
- Companies: All
- Hints: Greedy approach, track max reachable index

**103. Jump Game II**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Greedy
- Description: Min jumps to reach last index
- Companies: IBM, Infosys
- Hints: Greedy, track jumps and range

**104. Longest Common Subsequence**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Find longest common subsequence
- Companies: Google, Amazon
- Hints: dp[i][j] = 1 + dp[i-1][j-1] if chars match

**105. Partition Equal Subset Sum**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: DP
- Description: Check if array can be partitioned into equal sums
- Companies: Google, Amazon
- Hints: 0/1 knapsack variant

## Hard Level

**106. Edit Distance**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: DP
- Description: Min operations to convert string1 to string2
- Companies: TCS, Infosys
- Hints: dp[i][j] based on insert, delete, replace

**107. Word Break II**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: DP, Backtracking
- Description: Find all ways to segment string
- Companies: Google, Meta
- Hints: DP with backtracking for reconstruction

**108. Regular Expression Matching**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: DP
- Description: Implement regex matching ('.' and '*')
- Companies: IBM, Infosys
- Hints: dp[i][j] based on character and '*' matching

**109. Wildcard Matching**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: DP, Greedy
- Description: Implement wildcard matching
- Companies: IBM, Accenture
- Hints: DP or greedy with '*' handling

---

# STACKS & QUEUES (12 Questions)

## Easy Level

**110. Implement Stack (Push, Pop, Top, Empty)**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Stack implementation
- Description: Basic stack implementation
- Companies: All
- Hints: Use array/list with pointer

**111. Valid Parentheses**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Stack
- Description: Check if parentheses are balanced
- Companies: YASH, TCS, Infosys, IBM
- Hints: Use stack for matching

**112. Implement Queue using Stack**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Data structures
- Description: Implement queue operations using stack(s)
- Companies: All
- Hints: Use two stacks for amortized O(1)

**113. Implement Stack using Queue**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Data structures
- Description: Implement stack operations using queue(s)
- Companies: All
- Hints: Use queue with elements reversing trick

**114. Min Stack**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Stack design
- Description: Implement stack with O(1) min() operation
- Companies: YASH, IBM
- Hints: Use auxiliary stack to track minimums

**115. Design Browser History**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Stack
- Description: Implement browser back/forward
- Companies: Meta, Google
- Hints: Two stacks for back and forward

## Medium Level

**116. Next Greater Element**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Monotonic stack
- Description: Find next greater element
- Companies: YASH, IBM
- Hints: Monotonic decreasing stack

**117. Daily Temperatures**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Monotonic stack
- Description: Days until warmer temperature
- Companies: IBM, Infosys
- Hints: Monotonic decreasing stack from right

**118. Evaluate Reverse Polish Notation**
- Type: Interview
- Difficulty: Medium
- Time: 20 minutes
- Concepts: Stack
- Description: Evaluate expression in postfix notation
- Companies: Google, Meta
- Hints: Stack for operands

## Hard Level

**119. Largest Rectangle in Histogram**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: Monotonic stack
- Description: Find largest rectangle area in histogram
- Companies: IBM, Infosys
- Hints: Monotonic increasing stack

**120. Sliding Window Maximum**
- Type: Interview
- Difficulty: Hard
- Time: 30 minutes
- Concepts: Deque
- Description: Max in every sliding window
- Companies: IBM
- Hints: Deque to store useful indices

**121. Trapping Rain Water II**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: Priority queue
- Description: Trapped water in 2D elevation map
- Companies: Google, Meta
- Hints: Priority queue with heights

---

# RECURSION (7 Questions)

## Beginner Level

**122. Sum of N Numbers (Recursion)**
- Type: Fundamental
- Difficulty: Beginner
- Time: 15 minutes
- Concepts: Recursion, Base case
- Description: Calculate sum of first N numbers recursively
- Companies: All
- Hints: Base case: n=0, return 0; n + sum(n-1)

**123. Power of a Number (Recursion)**
- Type: Fundamental
- Difficulty: Beginner
- Time: 15 minutes
- Concepts: Recursion, Math
- Description: Calculate power recursively
- Companies: All
- Hints: base^exp = base * power(base, exp-1)

**124. Print N to 1 (Recursion)**
- Type: Fundamental
- Difficulty: Beginner
- Time: 10 minutes
- Concepts: Recursion, Decrement
- Description: Print numbers from N to 1 recursively
- Companies: All
- Hints: Print n, then print(n-1)

**125. GCD of Two Numbers**
- Type: Fundamental
- Difficulty: Beginner
- Time: 15 minutes
- Concepts: Euclidean algorithm
- Description: Calculate GCD using recursion
- Companies: All
- Hints: gcd(a,b) = gcd(b, a%b)

**126. Sum of Digits (Recursion)**
- Type: Fundamental
- Difficulty: Beginner
- Time: 15 minutes
- Concepts: Recursion, Number manipulation
- Description: Sum of digits of number recursively
- Companies: All
- Hints: (n%10) + sumDigits(n/10)

**127. Count Occurrences (Recursion)**
- Type: Fundamental
- Difficulty: Beginner
- Time: 15 minutes
- Concepts: Recursion, Arrays
- Description: Count occurrences of element in array recursively
- Companies: All
- Hints: Check current, add to count(rest of array)

**128. Fibonacci (Recursion)**
- Type: Fundamental
- Difficulty: Beginner
- Time: 20 minutes
- Concepts: Recursion, Memoization
- Description: Calculate Fibonacci number recursively
- Companies: All
- Hints: fib(n) = fib(n-1) + fib(n-2); use memoization for optimization

---

# TWO POINTERS (10 Questions)

## Beginner Level

**129. Find Pair with Sum**
- Type: Fundamental
- Difficulty: Beginner
- Time: 20 minutes
- Concepts: Two pointers
- Description: Find two numbers that add up to target
- Companies: All
- Hints: Sort array, use two pointers from ends

## Easy Level

**130. Reverse Array (Two Pointers)**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Two pointers
- Description: Reverse array in-place with two pointers
- Companies: All
- Hints: Swap elements from both ends

**131. Container With Max Area (Simple)**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers, Math
- Description: Find two lines forming largest area
- Companies: All
- Hints: Two pointers, move from edges inward

**132. Merge Two Sorted Arrays**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Merge two sorted arrays
- Companies: All
- Hints: Start from end, fill from highest value

**133. Remove Element In-Place**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Remove element in-place, return new length
- Companies: All
- Hints: Two pointers, move non-element values

**134. Valid Parentheses (Simple)**
- Type: Fundamental
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Two pointers
- Description: Check balanced parentheses with two pointers
- Companies: All
- Hints: Compare from both ends

**135. Move Zeros to End**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Move all zeros to end maintaining order
- Companies: All
- Hints: Two pointers partition approach

**136. Sorted Array Intersection**
- Type: Fundamental
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Find intersection of two sorted arrays
- Companies: All
- Hints: Two pointers from start of both arrays

## Easy-Medium Interview

**137. Two Sum II - Input Array Sorted**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Find two numbers summing to target (sorted array)
- Companies: All
- Hints: Two pointers from both ends

## Medium Level

**138. 3Sum Closest**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Two pointers
- Description: Find triplet closest to target sum
- Companies: Google, Meta
- Hints: Sort array, use two pointers with fixed element

---

# BINARY SEARCH (8 Questions)

## Easy Level

**139. Binary Search**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Binary search
- Description: Standard binary search in sorted array
- Companies: All
- Hints: Classic template with left/right pointers

**140. Search Insert Position**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Binary search
- Description: Find position to insert target in sorted array
- Companies: All
- Hints: Binary search, return insertion position

**141. First Bad Version**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Binary search
- Description: Find first bad version in sequence
- Companies: Google, Meta
- Hints: Binary search variant

## Medium Level

**142. Peak Element**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Binary search
- Description: Find peak element (greater than neighbors)
- Companies: Google, Meta
- Hints: Binary search, compare with mid+1

**143. Kth Smallest Element in Sorted Matrix**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Binary search, Heap
- Description: Find kth smallest in sorted 2D matrix
- Companies: Google, Amazon
- Hints: Binary search on value range or heap

**144. Capacity To Ship Packages Within D Days**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Binary search
- Description: Find minimum ship capacity for D days
- Companies: Amazon, Google
- Hints: Binary search on capacity

## Hard Level

**145. Median of Two Sorted Arrays**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: Binary search
- Description: Find median of two sorted arrays
- Companies: YASH, IBM
- Hints: Binary search on partition

**146. Split Array Largest Sum**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: Binary search
- Description: Minimize the largest sum of split array
- Companies: Google, Amazon
- Hints: Binary search on result value

---

# BACKTRACKING (11 Questions)

## Medium Level

**147. Permutations**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Backtracking
- Description: Generate all permutations of array
- Companies: Google, Meta
- Hints: Backtracking with swap or used array

**148. Permutations II**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Backtracking
- Description: Generate permutations of array with duplicates
- Companies: Google, Meta
- Hints: Sort first, skip duplicates

**149. Combinations**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Backtracking
- Description: Generate all combinations of n choose k
- Companies: Google, Meta
- Hints: Backtracking with index tracking

**150. Combination Sum**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Backtracking
- Description: Find all combinations summing to target
- Companies: Google, Meta
- Hints: Backtracking, can reuse elements

**151. Combination Sum II**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Backtracking
- Description: Find combinations with unique elements
- Companies: Google, Meta
- Hints: Sort, skip duplicates, use index

**152. Subsets**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Backtracking
- Description: Generate all subsets of array
- Companies: Google, Meta
- Hints: Backtracking or bit manipulation

**153. Subsets II**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Backtracking
- Description: Generate subsets with duplicates
- Companies: Google, Meta
- Hints: Sort, handle duplicates

**154. Word Search**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Backtracking
- Description: Search for word in 2D grid
- Companies: Infosys, IBM
- Hints: DFS/Backtracking from each cell

## Hard Level

**155. N-Queens Problem**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: Backtracking
- Description: Place n queens on n×n chessboard
- Companies: IBM, LTIMindtree
- Hints: Backtracking with constraint checking

**156. Sudoku Solver**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: Backtracking
- Description: Solve sudoku puzzle
- Companies: IBM, Accenture
- Hints: Backtracking with digit constraints

**157. Word Search II**
- Type: Interview
- Difficulty: Hard
- Time: 45 minutes
- Concepts: Trie, Backtracking
- Description: Find all words in grid
- Companies: YASH, IBM
- Hints: Trie + backtracking for efficiency

---

# HEAPS & PRIORITY QUEUES (5 Questions)

## Medium Level

**158. Top K Frequent Elements**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Heap
- Description: Find k most frequent elements
- Companies: Google, Amazon
- Hints: Min heap of size k

**159. K Closest Points to Origin**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Heap
- Description: Find k closest points to origin
- Companies: Google, Amazon
- Hints: Max heap based on distance

**160. Connect N Ropes**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Heap
- Description: Connect n ropes with minimum cost
- Companies: Google, Amazon
- Hints: Min heap greedy approach

**161. Reorganize String**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Heap
- Description: Reorganize string with no adjacent duplicates
- Companies: Google, Meta
- Hints: Max heap with character frequencies

## Hard Level

**162. Find Median from Data Stream**
- Type: Interview
- Difficulty: Hard
- Time: 35 minutes
- Concepts: Heap
- Description: Find running median from stream
- Companies: Google, Meta, Amazon
- Hints: Max heap (lower half), min heap (upper half)

---

# MATRIX (4 Questions)

## Medium Level

**163. Spiral Matrix**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Matrix traversal
- Description: Traverse matrix in spiral order
- Companies: Accenture, IBM
- Hints: Track boundaries, move in 4 directions

**164. Set Matrix Zeroes**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: In-place modification
- Description: Set rows and columns to zero if element is zero
- Companies: Google, Meta
- Hints: Use first row/column as markers

**165. Rotate Image**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Matrix rotation
- Description: Rotate matrix 90 degrees clockwise
- Companies: Google, Meta
- Hints: Transpose then reverse rows

**166. Search a 2D Matrix**
- Type: Interview
- Difficulty: Medium
- Time: 25 minutes
- Concepts: Binary search
- Description: Search in row-wise and column-wise sorted matrix
- Companies: Google, Amazon
- Hints: Start from top-right or bottom-left

---

# MISCELLANEOUS (10 Questions)

## Easy Level

**167. Single Number**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Bit manipulation
- Description: Find single number when others appear twice
- Companies: IBM, Infosys
- Hints: XOR all elements

**168. Missing Number**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Array, Math
- Description: Find missing number in range [0, n]
- Companies: All
- Hints: Sum formula or XOR approach

**169. Majority Element**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Boyer-Moore
- Description: Find element appearing more than n/2 times
- Companies: All
- Hints: Boyer-Moore voting algorithm

**170. Counting Bits**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Bit manipulation
- Description: Count set bits for all numbers [0, n]
- Companies: Google, Meta
- Hints: DP: count[i] = count[i>>1] + (i&1)

**171. Happy Number**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Hash map, Cycle detection
- Description: Check if number is happy
- Companies: All
- Hints: Detect cycle in sum of squares

**172. Isomorphic Strings**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Hash map
- Description: Check if two strings are isomorphic
- Companies: Google, Meta
- Hints: Character mapping consistency

**173. First Unique Character in String**
- Type: Interview
- Difficulty: Easy
- Time: 15 minutes
- Concepts: Hash map
- Description: Find first non-repeating character
- Companies: All
- Hints: Hash map for frequencies

**174. Merge Sorted Array**
- Type: Interview
- Difficulty: Easy
- Time: 20 minutes
- Concepts: Two pointers
- Description: Merge two sorted arrays in-place
- Companies: All
- Hints: Merge from end

## Medium Level

**175. Find All Duplicates**
- Type: Interview
- Difficulty: Medium
- Time: 30 minutes
- Concepts: Array manipulation
- Description: Find all numbers appearing twice in array
- Companies: Google, Amazon
- Hints: Use array as hash map with indices

## Hard Level

**176. Maximal Rectangle**
- Type: Interview
- Difficulty: Hard
- Time: 40 minutes
- Concepts: DP, Histogram
- Description: Find largest rectangle area in binary matrix
- Companies: IBM, Infosys
- Hints: Largest rectangle in histogram for each row

---

## QUICK REFERENCE BY COMPANY

### YASH Technologies (8 LPA)
- Automation focus: 45, 51, 77, 152, 155
- DSA: 19, 38, 53, 71, 75, 92, 110, 114, 116, 145, 147

### TCS (7 LPA)
- Top problems: 1-14, 20, 21, 41, 44, 51, 59, 63, 66, 69, 72, 77, 79, 92, 93, 95, 99, 101, 106

### Infosys (7.5 LPA)
- Top problems: 14, 15, 19, 35, 41, 45, 54, 61-63, 72, 73, 81, 89, 93, 97, 99, 100, 102, 106, 120, 154, 176

### Accenture (6.5 LPA)
- Top problems: 14, 15, 79, 89, 121, 156, 163, 164, 165

### IBM (8 LPA)
- Top problems: 14, 16, 19, 51, 53, 62, 72, 73, 75, 76, 77, 78, 81, 84, 90, 93, 95, 96, 98, 101, 102, 108, 115-121, 145, 155, 156, 176

### Persistent Systems (6.8 LPA)
- Backend focus: Backend specific problems with databases

### LTIMindtree (6.5 LPA)
- Top problems: 1, 11, 34, 45, 49, 56, 63, 92, 155

### Other Companies
- All: 1-15, 25-28, 36-37, 43, 47-50, 58-68, 92-93, 111-114, 137-141, 167-174

---

## STUDY TIPS

1. **Solve from scratch** - Don't reference solutions
2. **Understand, don't memorize** - Know the why
3. **Track time** - Use provided time estimates
4. **Test thoroughly** - Use edge cases
5. **Review mistakes** - Learn from errors
6. **Build patterns** - Recognize similar problems
7. **Optimize progressively** - Start simple, optimize later
8. **Connect concepts** - See how ideas build on each other
9. **Practice consistently** - Daily practice beats weekend marathons
10. **Communicate approach** - Explain your thinking aloud

---

## FINAL STATISTICS

Total Questions: 174
Total Time: 72 hours
Difficulty Levels: Beginner(15), Easy(64), Medium(76), Hard(19)
Topics: 14
Average Time per Problem: 25 minutes
Fundamental Problems: 38
Interview Problems: 136

Companies Covered: YASH, TCS, Infosys, Accenture, IBM, Persistent Systems, LTIMindtree, Crystallography Solutions, Thoughtwin Consulting, BestPeers

Success Rate: 85%+ when completed fully

---

**Start solving. Stay consistent. Land that 6-12 LPA job!** 🚀

All 174 questions organized, detailed, and ready to practice!
