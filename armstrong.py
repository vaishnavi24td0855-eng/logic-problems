num = int(input("Enter a number: "))

original = num
sum = 0
n = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + (digit ** n)
    num = num // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")