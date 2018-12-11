# The Goal: Inspired by Summer Son’s Mad Libs project with Javascript. The program
# will first prompt the user for a series of inputs a la Mad Libs. For example, a
# singular noun, an adjective, etc. Then, once all the information has been inputted,
# the program will take that data and place them into a premade story template.
# You’ll need prompts for user input, and to then print out the full story at the
# end with the input included.

## Pizza mad lib

adjectives = []
nationalities = []
personnames = []
nouns = []
numbers = []
foods = []
shapes = []

adjectives.append(input("Enter an adjective. "))
nationalities.append(input("Enter a nationality. "))
personnames.append(input("Enter a person's name. "))
nouns.append(input("Enter a noun. "))
adjectives.append(input("Enter an adjective. "))
nouns.append(input("Enter a noun. "))
adjectives.append(input("Enter an adjective. "))
adjectives.append(input("Enter an adjective. "))
nouns.append(input("Enter a noun. "))
nouns.append(input("Enter a noun. "))
numbers.append(input("Enter a whole number. "))
shapes.append(input("Enter a plural shape. "))
foods.append(input("Enter in a food. "))
foods.append(input("Enter in a food. "))
numbers.append(input("Enter a whole number. "))

pizza_madlib = """Pizza was invented by a {0} {1} chef named {2}.
                 To make a pizza you need to take a lump of {3},
                 and make a thin, round {4} {5}. Then you cover it with
                 {6} sauce, {7} cheese, and fresh chopped {8}. Next you
                 have to bake it in a very hot {9}. When it is done, cut
                 it into {10} {11}. Some kids like {12} pizza the best,
                 but my favorite is the {13} pizza. If I could, I would eat
                 pizza {14} times a day!""".format(adjectives.pop(0), nationalities.pop(0),
                 personnames.pop(0), nouns.pop(0), adjectives.pop(0), nouns.pop(0),
                 adjectives.pop(0), adjectives.pop(0), nouns.pop(0), nouns.pop(0), numbers.pop(0),
                 shapes.pop(0), foods.pop(0), foods.pop(0), numbers.pop(0))

print("Thank you. Enjoy this pizza madlib!")
print(pizza_madlib)
