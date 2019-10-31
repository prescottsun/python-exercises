def contains_second_power(list1, list2):
    for number in list1:
        if number ** 2 in list2:
            answer = True
        else:
            return False
    return answer

list1 = [1, 2, 3, 4]
list2 = [1, 4, 16, 9]

print(contains_second_power(list1, list2))