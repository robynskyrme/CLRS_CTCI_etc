# 11.3.2024
# Merge Sort

import random

def MergeSort(list):
    if len(list) == 1:
        return list

    result = []

    half = int(len(list)/2)

    left = MergeSort(list[:half])
    right = MergeSort(list[half:])

    total = len(left) + len(right)

    while len(result) < total:
        if left and right:
            if left[0] == right[0]:
                result.append(left[0])
                left = left[1:]
        if left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        if left and not right:
            result.append(left[0])
            left = left[1:]
        if right and not left:
            result.append(right[0])
            right = right[1:]


    return result


if __name__ == "__main__":

    for test in range(1000):

        list = []

        for j in range(19):
            list.append(random.randint(0,23))

        print(list)
        print(MergeSort(list))