#Mon 2018-10-08 12:01:26 MDT
# Assumption: Raw 3c = 1lb, Cooked = 2lbs 8oz @ 6.5c

import subprocess
subprocess.run("clear")

Labels = ["Cal", "Fat", "Carbs", "Fiber", "Protein", "Cost", "Weight"]
Black =   [170, .5, 31, 8, 11,     13.49, 10.0, 'Black'] #  10 lbs : 30c
Quinoa =  [190, 3.5, 33, 2, 6,      9.99,  4.5, 'Quinoa'] # 4.5 lbs : 13.5c
Masoori = [150, 0, 35, 0, 3,       14.99, 20.0, 'Masoori'] #  20 lbs : 60c
Soy =     [415, 18.5, 28, 8.5, 34, 22.00, 20.0, 'Soy'] #  20 lbs : 60c
Pinto =   [80, 1, 21, 12, 7,       23.00, 50.0, 'Pinto'] #  50 lbs : 150c
Pea =     [175, .5, 31, 7, 12,    25.00, 21.0, 'Pea']
IIFYM = [2274, 69, 243, 30, 171]
Serv = [0, 0, 0, 0, 0]

def recipe(x):
	sum = (tBlack*Black[x]) + (tQuinoa*Quinoa[x]) + (tMasoori*Masoori[x]) + (tSoy*Soy[x]) + (tPinto*Pinto[x]) + (tPea*Pea[x])
	return sum

def distance(x):
	if (recipe(x) > IIFYM[x]):
		return( "+" + str(recipe(x) - IIFYM[x]))
	elif (recipe(x) < IIFYM[x]):
		return( "-" + str(IIFYM[x] - recipe(x)))
	else:
		return

def price(VAR, tVAR):
	sum = round(((VAR[5]/(VAR[6]*3)) * (tVAR/4)), 2)
	return sum

def const(VAR, x):
	return ( str(VAR[x]) + ' ' + Labels[x] + ",")

def const2(VAR, x, y):
	if y == 1:
		dev = round( (VAR[2]/VAR[0]), 2)
	if y == 2:
		dev = round( (VAR[4]/VAR[0]), 2)
	return( str(VAR[x]) + ' ' + Labels[x] + " (" + str(dev) + "%), " )

def dev(VAR):
	dev1 = round( (VAR[0]/VAR[2]), 2)
	dev2 = round( (VAR[0]/VAR[4]), 2)
	return(VAR[7], "Protein dev HI: ", dev1, " .. Carb dev LO: ", dev2)


def sus(x, VAR, VAR2):
	MaxDeviation = 0.20
	if (VAR > VAR2):
		if (round((VAR2/VAR),2) > MaxDeviation ):
			return( distance(x) )
		if (round((VAR2/VAR),2) < MaxDeviation ):
			return( distance(x) + " Unsustainable")
	elif (VAR < VAR2):
		if ((1 - round((VAR/VAR2),2)) > MaxDeviation ):
			return( distance(x) + " Unsustainable")
		if ((1 - round((VAR/VAR2),2)) < MaxDeviation ):
			return( distance(x) )
	else:
		return

# Introduction
print("\n", "." * 45)
print("Recipe Calculator -- Written by Zac B")
print("." * 45, "\n")

# Print Constants
print("Black Beans (.25 cup): ", const(Black,0), const(Black,1), const2(Black,2,1), const(Black,3), const2(Black,4,2) )
print("Quinoa (.25 cup): ", const(Quinoa,0), const(Quinoa,1), const2(Quinoa,2,1), const(Quinoa,3), const2(Quinoa,4,2) )
print("Sona Masoori (.25 cup): ", const(Masoori,0), const(Masoori,1), const2(Masoori,2,1), const(Masoori,3), const2(Masoori,4,2) )
print("Soy (.25 cup): ", const(Soy,0), const(Soy,1), const2(Soy,2,1), const(Soy,3), const2(Soy,4,2) )
print("Pinto (.25 cup): ", const(Pinto,0), const(Pinto,1), const2(Pinto,2,1), const(Pinto,3), const2(Pinto,4,2) )
print("Pea (.25 cup): ", const(Pea,0), const(Pea,1), const2(Pea,2,1), const(Pea,3), const2(Pea,4,2) )
print("." * 45)

# Ratios
#print( "\n", dev(Black), "\n", dev(Quinoa), "\n", dev(Masoori), "\n", dev(Soy), "\n", dev(Pinto), "\n", dev(Pea) )

# Input Servings
tBlack = int(input("\nServings of Black Beans: "))
tQuinoa = int(input("Servings of Quinoa: "))
tMasoori = int(input("Servings of Sona Masoori: "))
tSoy = int(input("Servings of Soybeans: "))
tPinto = int(input("Servings of Pinto Beans: "))
tPea = int(input("Servings of Peas: "))
print("\n", "." * 45, "\n")

# Print Net Carbohydrates
nCarb = int(recipe(2) - recipe(3))


# Print Recipe Macros
print("Macros:")
print("Calories (" + str(IIFYM[0]) + "): ", recipe(0), sus(0, IIFYM[0], recipe(0)) )
print("Fat (" + str(IIFYM[1]) + "): ", recipe(1), sus(1, IIFYM[1], recipe(1)) )
print("Carbs (" + str(IIFYM[2]) + "): ", recipe(2), "(Net:" + str(nCarb) + ")", sus(2, IIFYM[2],recipe(2)) )
print("Fiber (" + str(IIFYM[3]) + "): ", recipe(3), sus(3, IIFYM[3],recipe(3)) )
print("Protein (" + str(IIFYM[4]) + "): ", recipe(4), sus(4, IIFYM[4],recipe(4)) )
print("\n", "." * 45, "\n")

# Print Recipe Cost
print("Price: ($" + str(round(price(Black,tBlack) + price(Quinoa,tQuinoa) + price(Masoori,tMasoori) + price(Soy,tSoy) + price(Pinto,tPinto), 2)) + ")" )
print("Black Beans: ($" + str(price(Black, tBlack)) + ")" )
print("Quinoa: ($" + str(price(Quinoa, tQuinoa)) + ")" )
print("Masoori: ($" + str(price(Masoori, tMasoori)) + ")" )
print("Soybeans: ($" + str(price(Soy, tSoy)) + ")" )
print("Pinto: ($" + str(price(Pinto, tPinto)) + ")" )
print("Pea: ($" + str(price(Pea, tPea)) + ")" )
print("\n", "." * 45, "\n\n")
