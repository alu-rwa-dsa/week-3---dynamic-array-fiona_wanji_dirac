# associative list
# we begin by creating an associative list that has a person's name and their age
ages = {"Lucy": 56,
        "Tattiana": 5,
        "Rudi": 26,
        "Jeff": 38}


# add(key,value)


def add_age(dict, person, age):
    dict[person] = age
    print("New list after adding is: ")
    for a, b in dict.items():
        print(a, b)


# remove(key)
def remove_age(dict, person):
    del dict[person]
    print("New list after removing is: ")
    for a, b in dict.items():
        print(a, b)


# modify(key,newvalue)
def change_age(dict, person, age):
    dict[person] = age
    print("New list after modifying is: ")
    for a, b in dict.items():
        print(a, b)


# lookup(key)
def lookup_age(dict, person):
    print("The age of the person is " + str(dict.get(person)))
    return dict.get(person)


# we print the original associative list
print("Original list is")
for k, v in ages.items():
    print(k, v)

# we test the methods
add_age(ages, "Angie", 25)
remove_age(ages, "Lucy")
change_age(ages, "Angie", 35)
lookup_age(ages, "Angie")