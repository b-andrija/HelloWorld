pinnr = 0

while True:
    userpin = input("PIN: ")
    pinnr += 1

    if userpin == "4321" and pinnr == 1:
        print("Correct! It only took you one single attempt!")
        break

    elif userpin == "4321":
        print(f"Correct! it took you {pinnr} attempts")
        break

else:
    print("Wrong")