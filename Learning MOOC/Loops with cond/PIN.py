attempts = 3

while True:

    code_setup = int(input("Please create a new PIN: "))

    if len(str(code_setup)) != 4:
        print("PIN has to be 4 digits!")
    elif len(str(code_setup)) == 4:
        break


while True:
    code = int(input("Please type in your PIN: "))

    if code_setup == code:
        print("Correct PIN, Access granted")
        break
    elif code_setup != code:
        attempts -= 1
        if attempts == 2 or attempts == 1:
            print(f"Invalid PIN, you have {attempts} more attempts")
        if attempts == 0:
            print("Your account is blocked")
            break
