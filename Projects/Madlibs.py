STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s s ruled the world."

print('The game has begun.')
print(STORY)

name = input('Enter a name:')

adj1 = input('First ajective:')
adj2 = input('Second adjective:')
adj3 = input('Third adjective:')

verb = input("One verb:")

noun1 = input("First noun:")
noun2 = input ("Second noun:")

animal = input("Enter an animal:")
food = input('Enter a food:')
fruit = input('Enter a fruit:')
superhero = input('Enter a superhero:')
country = input('Enter a coutry:')
dessert = input('Enter a dessert:')
year = input('Enter a year:')


print (STORY % ( name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))
