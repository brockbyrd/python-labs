friends = ["Dustin", "Sam", "Cole", "Alex"]
lucky_numbers = [2, 4, 7, 9, 13, 18, 24]

print(friends[3])

#grabs elements after index of 1
print(friends[1:])

#grabs elements after index of 1 up to 2
print(friends[1:3])

#extend function to add llst to list
#friends.extend(lucky_numbers)

#add to end of list
#friends.append("Creed")

#add item to middle of list
#friends.insert(1, "Kelly")

#remove item from list
#friends.remove("Cole")

#clear list
#friends.clear()

#removes last element
#friends.pop()

#finds elements in list at index
print(friends.index("Sam"))

#finds number of time a value is in a list
print(friends.count("Alex"))

#alphabetical order and ascending order
print(friends.sort())

#reverse list order
print(friends.reverse())

#copy list
friends2 = friends.copy()