print("Please type in integer number. Type 0 to finish")
count = 0
sum = 0
negnumma = 0
posnumma = 0

while True:
    numma = int(input("Number: "))
    count += 1
    sum = numma + sum
    if numma == 0:
        break
    mean = sum / count
    if numma <0:
        negnumma += 1
    if numma >0:
        posnumma += 1

    print(f"Numbers typed in {count}")
    print(f"The sum of the numbers is {sum}")
    print(f"The mean of the numbers is {mean}")
    print(f"Positive numbers {posnumma}")
    print(f"Negative numbers {negnumma}")
