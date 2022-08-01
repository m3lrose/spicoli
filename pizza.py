import time
import random


welcome = "Sup brah,  welcome to the zah huzzah"
print (welcome)
time.sleep(1)

zahornah = input("Yo brah, are you looking for some zah or nah?: ")
if zahornah  == "zah":
	print("What area do you want zah brah?")

elif zahornah == "nah":
	print  ("Sorry to hear that brah")
else:
	print("Please answer zah or nah, brah!")







Downtown = ['Pizzeria Di Giovanni', 'Renzo', 'Melfis', 'DAllesandro', 'Frannie and the Fox', 'Monza',  'Benny Ravellos', 'Sabatinos  Pizza', 'Baker and Brewer', 'Uneeda Sicilian', 'Renzo', 'Baked Pizzeria']
print(random.choice(Downtown))

WestAshley = ['Slice', 'Marios',  'Baronis', 'Andolinis']
print(random.choice(WestAshley))

NCharleston = ['Evo Pizzeria', 'Park Pizza Co']
print(random.choice(NCharleston))

JamesIsland = ['Famiularis Pizzeria', 'Crust Wood Fired Pizza', 'Dough Boy', 'Paisanos Pizza Grill']
print(random.choice(JamesIsland))

MtPleasant =  ['La  Pizzeria', 'The Obstinate Daughter']
print(random.choice(MtPleasant))

DanielIsland = ['Vespa  Pizzeria', 'Orlandos  Pizza']
print(random.choice(DanielIsland))


