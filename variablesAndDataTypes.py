#variables and data types
character_name = "Brock"
character_age = "22"
is_male = True

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + character_age + ".")

#working with strings
phrase = "Flatiron School"

print("Flatiron\nSchool")
print("Flatiron\'School")
print(phrase + " is awesome.")
print(phrase.lower())
print(phrase.upper())

print(phrase.islower())
print(phrase.upper().isupper())

#getting the length of a string
print(len(phrase))
#getting a character at specified index
print(phrase[0])
#finds index of character in phrase
print(phrase.index("o"))
#replace function to replace character or phrase
print(phrase.replace("School", "Academy"))

#working with numbers
