is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or you are tall or both")
else:
    print("You are not a male or tall")

if is_male and is_tall:
    print("You are a male and you are tall")
elif is_male and not(is_tall):
    print("You are a male and you are not tall")
elif not(is_male) and is_tall:
    print("You are not a male and you are tall")
else:
    print("You are not a male or you are not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(71, 1, 9))

def animal(pet):
    if pet == "dog":
        print("Woof")
    elif pet == "cat":
        print("Meow")
    elif pet == "bird":
        print("Tweet")
    else:
        print("I'm not sure what sound that animal makes.")

animal("lion")


i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with while loop")


for letter in "Flatiron School":
    print(letter)


friends = ["Dustin", "Sam", "Cole", "Alex"]
for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")

#exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 3))