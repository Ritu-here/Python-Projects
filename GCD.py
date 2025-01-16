# write a program to find the greatest common divisor of two number
x = int(input("Enter the first number"))
y= int(input("Enter the second number"))
gcd=0
for i in range(min(x,y)+1):
    if(x%i == 0 and x%i == 0):
        gcd=i
print("GCD = ", gcd )
