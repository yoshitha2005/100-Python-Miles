num = int(input("Enter a number: "))
sum_digits = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print("Sum of digits:", sum_digits)
