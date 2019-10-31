def same_freq(a1, a2):
    sorted_a1 = sorted(a1)
    sorted_a2 = sorted(a2)
    if sorted_a1 == sorted_a2:
        return True
    else:
        return False


list1 = [1, 2, 3, 4]
list2 = [1, 4, 3, 3]

print(same_freq(list1, list2))