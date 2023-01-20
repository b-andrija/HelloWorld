InString = input("Please type in a word: ")
InWord = input("Please type in a character: ")

IndexLoc = InString.find(InWord)
IndexLoc = InString[IndexLoc:]
if len(IndexLoc[:3]) == 3:
    print(IndexLoc[:3])

#Programming exercise:
#Find the first substring