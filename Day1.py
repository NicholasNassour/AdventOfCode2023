f = open("Day1_puzzle_input.txt", "r")
sum = 0
for line in f:
    num = [-1,-1]
    for char in line:
        if char.isdigit():
            if num[0] == -1:
                num[0] = char
            else:
                num[1] = char
    if num[1] == -1:
        sum += int(num[0]) * 10 + int(num[0])
    else:
        sum += int(num[0]) * 10 + int(num[1])

print(sum)