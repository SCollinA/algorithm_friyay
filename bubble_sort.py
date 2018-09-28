# take each number and compare to next number
# from time import sleep

num_list = [9, 7, 8, 1, 3, 6, 5, 10, 2, 4]

def bubble_sort(list_to_sort):
    for j in range(len(list_to_sort)):
        # every time it goes through loop it should goes through 1 less time
        for i in range(len(list_to_sort) - 1 - j):
            # if first number is larger
            if list_to_sort[i] > list_to_sort[i + 1]:
                # swap
                # temp_num = list_to_sort[i + 1]
                # list_to_sort[i + 1] = list_to_sort[i]
                # list_to_sort[i] = temp_num
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            # print(list_to_sort)
            # sleep(1)
        # print()
        # print(list_to_sort)
        # print()
        # sleep(.5)
    return list_to_sort

print(bubble_sort(num_list))