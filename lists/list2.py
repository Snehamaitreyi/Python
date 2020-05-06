#shopping at the market


"""def sum(numbers):
    total =0
    for number in numbers:
        total+=number
    return total

n=[1,2,3,4,5,6]
print(sum(n))"""

list=['banana','orange','apple']
prices = {
    "banana":4,
    "orange":1.5,
    "apple":2,
    "berry":10
}
stock = {
    "banana":12,
    "orange":5,
    "apple":1,
    "berry":6
}
def bill(food):
    total=0
    for item in food:
        if stock[item]>0:
          total+=prices[item]
          stock[item]-=1
    return total

print(bill("apple"))

