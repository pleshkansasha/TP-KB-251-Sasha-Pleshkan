def find_position(numbers, value):
    for i in range(len(numbers)):
        if value < numbers[i]:
            return i
    return len(numbers)
numbers = ["aa", "ee", "zz"]
value = input("New value: ")
position = find_position(numbers, value)
numbers.insert(position, value)
print(numbers)