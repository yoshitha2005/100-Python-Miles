
num = int(input("Enter a number: "))
temp = num
order = len(str(num))
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if sum_val == num:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
