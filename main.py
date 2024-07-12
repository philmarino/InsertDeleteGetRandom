import random

class RandomizedSet(object):

    def __init__(self):
        self.list = []
        return

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.list:
            return False
        else:
            self.list.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.list:
            self.list.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


#Example 1:
#Input
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1)) #Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2)) #Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2)) #Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom()) #getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1)) #Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2)) #2 was already in the set, so return false.
print(randomizedSet.getRandom()) #Since 2 is the only number in the set, getRandom() will always return 2.
#["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
#[[], [1], [2], [2], [], [1], [2], []]
#Output
#[null, true, false, true, 2, true, false, 2]

#Explanation
#RandomizedSet randomizedSet = new RandomizedSet();
#randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
#randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
#randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
#randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
#randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
#randomizedSet.insert(2); // 2 was already in the set, so return false.
#randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

#Constraints:
#-231 <= val <= 231 - 1
#At most 2 * 105 calls will be made to insert, remove, and getRandom.
#There will be at least one element in the data structure when getRandom is called.
