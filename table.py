num = int(input("enter the number:"))
def table_display(n):
    for i in range(1,11):
        print(n,"*",i, "=",n*i)
print(table_display(num))
