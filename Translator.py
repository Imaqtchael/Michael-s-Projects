def translator(phrase = input("Enter the word you want to translate: ")):
    translation = ""
    for x in phrase:
        if x.lower() in "aeiou":
            if x.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + x
    print(translation)
translator()