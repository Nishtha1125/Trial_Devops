x = int(input('Enter x : '))
y = int(input('Enter y : '))
z = int(input('Enter z : '))

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)