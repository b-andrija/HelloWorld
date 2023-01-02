words = ""
lastword = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or word == lastword:
        print(words)
        break
    if word != "end:":
        words += word + " "

    lastword = word
