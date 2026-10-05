def duplicates(lst):
    count = {}
    duplicate = []

    for num in lst:
        count[num] = count.get(num, 0)+1

    for num in count:
        if count[num] > 1:
            duplicate.append(num)

    return sorted(duplicate)

numbers = [2,34,2,1,46,7,8,2,8]
print(duplicates(numbers))
        


