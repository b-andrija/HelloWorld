from math import sqrt

while True:
    numma = int(input("Please type in a number: "))
    if numma < 0:
        print("Invalid number! ")
    elif numma > 0:
        print(sqrt(numma))
    elif numma == 0:
        break
print("Exiting...")