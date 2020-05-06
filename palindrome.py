num =int(input("enter the number:"))
def palidrom(n):
    if n== n[::-1]:
        print(" palindrom")

    else:
        print("num is not a palindrom")
print(palidrom(num))
