import time
import random
import csv

"""
arestaurants = {}
for name in restaurants.csv:
	arestaurants[restaurantname] = Restaurant()
"""

def WASelect():
	with open('restaurants.csv', newline='') as f:
		reader = csv.reader(f)
		for row in reader:
				if "West Ashley" in row:
					print(row)
"""
def main():/

	welcome = "Sup brah,  welcome to the zah huzzah"
	print (welcome)
	time.sleep(0.25)

	zahornah = input("Yo brah, are you looking for some zah or nah?: ")
	if zahornah  == "zah":
		print("What area do you want zah brah?")
		print("\t1. Downtown\n\t2. West Ashley\n\t3. Mt Pleasant\n\t4. North Charleston\n\t5. James Island\n\t6. Daniel Island\n")
		input("::>")

	elif zahornah == "nah":
		print  ("Sorry to hear that brah")
	else:
		print("Please answer zah or nah, brah!")
print(restaurants)
main()
"""