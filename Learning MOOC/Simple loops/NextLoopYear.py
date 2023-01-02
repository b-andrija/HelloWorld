
year = int(input("Year: "))
year2 = year

while True:
    year2 += 1

    if year2 % 4 == 0 and (year2 % 100 != 0 or year2 % 400 == 0):
        print(f"The next leap year after {year} is {year2}")
        break