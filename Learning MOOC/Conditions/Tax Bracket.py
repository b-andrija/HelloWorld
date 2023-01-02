tax = float(input("Value of gift: "))

if tax < 5000:
    print("No tax!")

elif tax <= 25000:
    tax = 100 + (tax - 5000) * 0.08
    print(f"Amount of tax: {tax} euros")

elif tax <= 55000:
    tax = 1700 + (tax - 25000) * 0.10
    print(f"Amount of tax: {tax} euros")

elif tax <= 200000:
    tax = 4700 + (tax - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")

elif tax <= 1000000:
    tax = 22100 + (tax - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")

elif tax > 1000000:
    tax = 142100 + (tax - 1000000 ) * 0.17
    print(f"Amount of tax: {tax} euros")