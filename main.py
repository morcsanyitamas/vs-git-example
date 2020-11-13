numbers = [1, 2, 3, 4, 5, 6]
letters = ['a', 'b']


def get_length(list):
    count = 0
    for element in list:
        count += 1
    return count


length = get_length(letters)
print(length)