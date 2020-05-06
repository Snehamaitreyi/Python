str = "welcome to wonder world"
print(str.capitalize())
print(str.title())
print(str.isupper())
print(str.upper())
print(str.lower())
print(str.islower())
str1="HeLo! Hola"
print(str1.swapcase())
print(str1.replace('Hola','good morning'))
#ascending order
print("".join(sorted(str)))
#descending order
print(''.join(reversed(sorted(str))))
#reverse
print(''.join(reversed(str)))

#print with ....
print('...'.join(str))

str2="python easy"
print(str2[0:6])
#or
b=str2.split('e')[0]
print(b)
#or
print(str2.replace('python',''))