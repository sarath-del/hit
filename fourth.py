
def is_armstrong_number(num):
    digit_sum = sum([int(digit)**3 for digit in str(num)])
    return digit_sum == num
N = int(input())
values = []
for i in range(N):
    values.append(int(input()))

for i in range(N):
    if is_armstrong_number(values[i]):
        values[i] = 1
    else:
        values[i] = 0


print( values)