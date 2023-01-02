word = input("Please type in a string: ")

if word[1] != word[4]:
    print("The second and second to the last characters are different")
else:
    print(f"The second and the second to the last characters are {word[1]}")



print("Time for second part, by second part I mean second script.")

while True:
    firstword = input("Please type in a your password: ")
    var = len(firstword)

    print(firstword)
    print("*" * var)


    if firstword == "":
        break
