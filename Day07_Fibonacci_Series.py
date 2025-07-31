n = int(input("Enter a number: "))
a, b = 0, 1
print(f"Fibonacci numbers up to {n}:", end=" ")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
