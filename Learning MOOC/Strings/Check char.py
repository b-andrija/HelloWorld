word1 = input("Please type in a string: ")

if word1[1] == word1[-2]:
    print(f"The second and the second to last characters are {word1[1]}")
else:
    print("The second and the second to last characters are different")