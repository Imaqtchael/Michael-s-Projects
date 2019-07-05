"Format Method"""
num = 50
years = 2040
country = "California"
sentence = "I want to have {0} when I go to {1} in the year {2}." #where the number inside the brackets are index
print(sentence.format(num, country, years))
"Pop method (List)"
x = ["Kirwen", "Michael", "bobo", "Jeirco"]
x.pop(1)
print(x)
"Del method (List)"
x = ["bobo", "si", "kiwen"]
del x[2]
print(x)
"""del x will delete the variable itself,  will return an error
print(x)"""
"Clear method (List)"
x = ["michael", "Kirwen"]
x.clear()
print(x)