# 12.3.2024
# Insertion Sort

import random

                            # simple method to swap two items in a list
def swap(list,a,b):
    old_a = list[a]
    list[a] = list[b]
    list[b] = old_a

def InsertionSort(list):
                            # Start with the second item (we will check to its immediate left)
    key = 1

                            # While condition to loop through each item in turn
    while key < len(list):
                            # If it's in the right place, no code runs
                            # If it needs to be swapped to the left...
        if list[key-1] > list[key]:
                            # We swap it leftwards, and keep swapping leftwards until it is in the right place
            trackback = key
            while trackback > 0 and list[trackback-1] > list[trackback]:
                swap(list,trackback-1,trackback)
                trackback -= 1

        key += 1

    return list




if __name__ == "__main__":
    for test in range(123):

        list = []

        for j in range(19):
            list.append(random.randint(0,23))

        print(InsertionSort(list))