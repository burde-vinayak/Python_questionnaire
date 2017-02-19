class item_store:

    def __init__(self, items=None):
        if items is None:
            self.list_items = []
            self.freq_counter = {}
        else:
            self.freq_counter = {}
            self.list_items = items
            # Create a frequency counter dictionary - O(n) time complexity
            for item in self.list_items:
                if item in self.freq_counter:
                    self.freq_counter[item] += 1
                else:
                    self.freq_counter[item] = 1

    def store_items(self, list_items):
        self.list_items = list_items
        for item in self.list_items:
            if item in self.freq_counter:
                self.freq_counter[item] += 1
            else:
                self.freq_counter[item] = 1

    def append(self, new_item):
        if new_item in self.freq_counter:
            self.freq_counter[new_item] += 1
        else:
            self.freq_counter[new_item] = 1
        self.list_items.append(new_item)

    def delete(self, item_val):
        if item_val in self.freq_counter:
            self.freq_counter[item_val] -= 1
            if self.freq_counter[item_val] == 0:
                del self.freq_counter[item_val]
        else:
            return -999999
        ret_val = self.list_items.remove(item_val)
        return ret_val

    def unique_items(self):
        res_list = []
        for k in self.freq_counter:
            res_list.append(k)
        return res_list

    def item_frequencies(self):
        return self.freq_counter

    def return_item_list(self):
        return self.list_items

arr = [1, 2, 3, 1, 5, 6, 5]
IS = item_store(arr)
unique = IS.unique_items()
freq = IS.item_frequencies()
print unique
print freq

# Append new items and check
IS.append(6)
IS.append(8)
unique = IS.unique_items()
freq = IS.item_frequencies()
print unique
print freq

# Delete items and check
IS.delete(1)
IS.delete(8)
unique = IS.unique_items()
freq = IS.item_frequencies()
print unique
print freq
print IS.return_item_list()