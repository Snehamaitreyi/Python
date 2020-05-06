num = int(input("Enter the number:"))
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            print(num,"is not  a prime number")
            break
        else:
            print(num,"is a prime number")
print(prime(num))