
def alphabet_position(text):
        text=text.lower()
        text = text.replace(" ", "")
        for element in text:
            if element=="a":
                text=text.replace("a","1 ")
            elif element=="b":
                text = text.replace("b", "2 ")
            elif element == "c":
                text = text.replace("c", "3 ")
            elif element == "d":
                text = text.replace("d", "4 ")
            elif element == "e":
                text = text.replace("e", "5 ")
            elif element == "f":
                text = text.replace("f", "6 ")
            elif element == "g":
                text = text.replace("g", "7 ")
            elif element == "h":
                text = text.replace("h", "8 ")
            elif element == "i":
                text = text.replace("i", "9 ")
            elif element == "j":
                text = text.replace("j", "10 ")
            elif element == "k":
                text = text.replace("k", "11 ")
            elif element == "l":
                text = text.replace("l", "12 ")
            elif element == "m":
                text = text.replace("m", "13 ")
            elif element == "n":
                text = text.replace("n", "14 ")
            elif element == "o":
                text = text.replace("o", "15 ")
            elif element == "p":
                text = text.replace("p", "16 ")
            elif element == "q":
                text = text.replace("q", "17 ")
            elif element == "r":
                text = text.replace("r", "18 ")
            elif element == "s":
                text = text.replace("s", "19 ")
            elif element == "t":
                text = text.replace("t", "20 ")
            elif element == "u":
                text = text.replace("u", "21 ")
            elif element == "v":
                text = text.replace("v", "22 ")
            elif element == "w":
                text = text.replace("w", "23 ")
            elif element == "x":
                text = text.replace("x", "24 ")
            elif element == "y":
                text = text.replace("y", "25 ")
            elif element == "z":
                text = text.replace("z", "26 ")
            elif not(element)==" " :
                text = text.replace(element, "" )
        text=text[:-1]
        return text
pass





aString=input("Give me a string: \n")
newstring=alphabet_position(aString)
print(newstring)