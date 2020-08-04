import time
from collections import Counter



#! Opening Txt Files for Names
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#! Literal trash
# start_time = time.time()
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# Starting Method is 7.330885648727417 seconds
# end_time = time.time()
# print("=========================================================================================================")
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
# print("=========================================================================================================")

#! Binary Search Tree Start
start_time = time.time()
class BSTNode:
    def __init__(self, name):
        self.value = name
        self.left = None
        self.right = None

    def insert(self, new_name):
        #? Go Left
        if new_name < self.value:
            if self.left is None:
                self.left = BSTNode(new_name)
            else:
                self.left.insert(new_name)
        #? Go Right
        if new_name > self.value:
            if self.right is None:
                self.right = BSTNode(new_name)
            else:
                self.right.insert(new_name)

    def contains(self, target):
        #? Found it
        if target == self.value:        
            return True
        #? Go Left
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        #? Go Right
        else:
            if self.right is None:
                return False
            else:  
                return self.right.contains(target)
    #// def getorder(self):
    #//     if self.left:
    #//         self.left.getorder()
    #//     print(self.value),
    #//     if self.right:
    #//         self.right.getorder()

tree = BSTNode(names_1[0])
for name in names_1:
    tree.insert(name)

#// tree.getorder()

duplicates = [name for name in names_2 if tree.contains(name)]

end_time = time.time()
print("=========================================================================================================")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print("=========================================================================================================")



#! ---------- Stretch Goal -----------
#! Python has built-in tools that allow for a very efficient approach to this problem
#! What's the best time you can accomplish?  Thare are no restrictions on techniques or data
#! structures, but you may not import any additional libraries that you did not write yourself.

#! Using Counter elements
# start_time = time.time()
# duplicates = list((Counter(names_1) & Counter(names_2)).elements())
# # runtime: 0.0070531368255615234 seconds
# end_time = time.time()
# print("=========================================================================================================")
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
# print("=========================================================================================================")

#! Using Set Function
start_time = time.time()
duplicates = set(names_1) & set(names_2)
# runtime: 0.003999233245849609 seconds
end_time = time.time()
print("=========================================================================================================")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print("=========================================================================================================")


