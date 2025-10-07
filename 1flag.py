def flag(hight, len):
    for red in range(hight):
        for l in range(len+1): print(u"\u001b[41m \u001b[0m", end="")
        print("")
    for wight in range(hight):
        for l in range(len+1): print(u"\u001b[47m \u001b[0m", end="")
        print("")
    for blue in range(hight):
        for l in range(len+1): print(u"\u001b[44m \u001b[0m", end="")
        print("")

hight = int(input("Укажите высоту цвета флага: "))
len = int(input("Укажите длину цвета флага: "))

flag(hight, len)