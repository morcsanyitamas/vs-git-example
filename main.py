numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
letters = ['a', 'b', 'c']
x = [10, 11, 20, 30, 40, 70, 980]

def get_length(list):
    count = 0
    while list != []:
        list.pop(0)
        count += 1
    return count


length = get_length(numbers)
print(length)