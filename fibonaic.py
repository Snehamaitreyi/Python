num = int(input("enter number:"))
def fibonaic(n):
    t1=0
    t2 =1
    for i in range(n):
        temp = t1+t2
        t1=t2
        t2 = temp
        if t1>=n:
            break
        print(t1)
print(fibonaic(num))