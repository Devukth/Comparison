print("Comparison")
print("Say any two numbers, and we'll check if they're equal, greater, or lesser.")
num1 = int(input("First Number ---> "))
num2 = int(input("Second Number ---> "))
if (num1 > num2):
    print("%d is greater than %d" %(num1, num2))
elif (num1 == num2):
    print("%d is equal to %d" %(num1, num2))
elif (num1 < num2):
    print("%d is lesser than %d" %(num1, num2))