# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
# Implement a function likes :: [String] -> String, which must take in input array, 
# containing the names of people who like an item. 
# For 4 or more names, the number in and 2 others simply increases.

def likes(names):
# if names is less than 3
# if names is 1, then name + " likes this"
# if names is 2, then name[0] + " and " + name[1] + " like this"
# if names is 3, then name[0] + ", " + name[1] + " and " + name[2] + " like this"
    if len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif len(names) >= 4:
        return names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"
    else:
        return("no one likes this")