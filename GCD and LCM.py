
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b


while y != 0:
    temp = y
    y = x % y
    x = temp

gcd = x


lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)