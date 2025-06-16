# intersection of Two Arrays

# def intersect(nums1, nums2):
#     if not nums1 or not nums2:
#         return []
    
#     res = []
#     count = {}
    
#     for num in nums1:
#         count[num] = count.get(num, 0) + 1
        
#     for num in nums2:
#         if num in count and count[num] > 0:
#             res.append(num)
#             count[num] -= 1
            
#     return res

# print(intersect([1,2,2,1], [2,2]))  # → [2, 2]
# print(intersect([4,9,5], [9,4,9,8,4]))  # → [4,9] o [9,4]


# Valid Anagram

# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
    
#     count = {}
    
#     for char in s:
#         count[char] = count.get(char, 0) + 1
    
#     for char in t:
#         if char not in count or count[char] == 0:
#             return False
#         count[char] -= 1
        
#     return True
    
# print(isAnagram("listen", "silent"))  # True
# print(isAnagram("rat", "car"))        # False
# print(isAnagram("aacc", "ccac"))      # False


# Two Sum

def TwoSum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
        
#First unique Character in a Sring

def first_unique(s):
    if not s:
        return -1
    
    count = {}
    
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    
    return -1


print(first_unique("leetcode"))       # 0
print(first_unique("loveleetcode"))   # 2
print(first_unique("aabb"))           # -1

    
    

