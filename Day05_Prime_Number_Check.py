def primeornot(num):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                print(f"The given number {num} is not a prime number")
                break
        else:
                print(f"The given number {num} is a prime number")
    else:
        print("Please enter a number between 2 and infinity!!")
a=int(input("Enter a number : "))
result=primeornot(a)