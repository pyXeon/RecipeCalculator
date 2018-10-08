# Python 3.6.1
# import subprocess
# subprocess.run("clear")

Labels = ["Cal", "Fat", "Carbs", "Fiber", "Protein", "Cost", "Weight"]
Black =   [170, .5, 31, 8, 11,     13.49, 10.0, 'Black'] #  10 lbs : 30c
Quinoa =  [190, 3.5, 33, 2, 6,      9.99,  4.5, 'Quinoa'] # 4.5 lbs : 13.5c
Masoori = [150, 0, 35, 0, 3,       14.99, 20.0, 'Masoori'] #  20 lbs : 60c
Soy =     [415, 18.5, 28, 8.5, 34, 22.00, 20.0, 'Soy'] #  20 lbs : 60c
Pinto =   [80, 1, 21, 12, 7,       23.00, 50.0, 'Pinto'] #  50 lbs : 150c
Pea =     [175, .5, 31, 7, 12,    25.00, 21.0, 'Pea'] # Test
IIFYM = [2274, 69, 243, 30, 171] #Alter these numbers based on person macro count
Serv = [2, 1, 2, 4, 1, 0]
MaxDeviation = 0.20

def recipe(x): # Multiply servings variable by ingredient macro values | Return total
	sum = (Serv[0]*Black[x]) + (Serv[1]*Quinoa[x]) + (Serv[2]*Masoori[x]) + (Serv[3]*Soy[x]) + (Serv[3]*Pinto[x]) + (Serv[4]*Pea[x])
	return sum

def distance(x): # Distance of IIFYM value from Recipe value
	if (recipe(x) > IIFYM[x]):
		return( "+" + str(recipe(x) - IIFYM[x]))
	elif (recipe(x) < IIFYM[x]):
		return( "-" + str(IIFYM[x] - recipe(x)))
	else:
		return

def price(VAR, tVAR): # 1. Find $/cup | 2. Multiply by servings | 3. Round to nearest hundredth
	sum = round(((VAR[5]/(VAR[6]*3)) * (tVAR/4)), 2)
	return sum

def const(VAR, x, y, z): # VAR = ingredient | x = Macro | y = Protein / Carb | z = Boolean, print percentage?
	if z == True:
		if y == 1:
			dev = round( (VAR[2]/VAR[0]), 2)
		if y == 2:
			dev = round( (VAR[4]/VAR[0]), 2)
		return( str(VAR[x]) + ' ' + Labels[x] + " (" + str(dev) + "%), " )
	else:
		return( str(VAR[x]) + ' ' + Labels[x] + ",")

def sus(x, VAR, VAR2): # Determine Sustainability | If the distance is greater than given MaxDeviation, print Unsustainable
	if (VAR > VAR2):
		if (round((VAR2/VAR),2) > MaxDeviation ):
			return( distance(x) )
		if (round((VAR2/VAR),2) < MaxDeviation ):
			return(" (Unsustainable " + distance(x) + ")")
	elif (VAR < VAR2):
		if ((1 - round((VAR/VAR2),2)) > MaxDeviation ):
			return(" (Unsustainable " + distance(x) + ")")
		if ((1 - round((VAR/VAR2),2)) < MaxDeviation ):
			return( distance(x) )
	else:
		return

# Print Introduction
print("\n", "." * 45)
print("Recipe Calculator -- Written by Zac B")
print("." * 45, "\n")

# Print Ingredient Constants
print("Black Beans (.25 cup): ", const(Black,0,0,0), const(Black,1,0,0), const(Black,2,1,1), const(Black,3,0,0), const(Black,4,2,1) )
print("Quinoa (.25 cup): ", const(Quinoa,0,0,0), const(Quinoa,1,0,0), const(Quinoa,2,1,1), const(Quinoa,3,0,0), const(Quinoa,4,2,1) )
print("Sona Masoori (.25 cup): ", const(Masoori,0,0,0), const(Masoori,1,0,0), const(Masoori,2,1,1), const(Masoori,3,0,0), const(Masoori,4,2,1) )
print("Soy (.25 cup): ", const(Soy,0,0,0), const(Soy,1,0,0), const(Soy,2,1,1), const(Soy,3,0,0), const(Soy,4,2,1) )
print("Pinto (.25 cup): ", const(Pinto,0,0,0), const(Pinto,1,0,0), const(Pinto,2,1,1), const(Pinto,3,0,0), const(Pinto,4,2,1) )
print("Pea (.25 cup): ", const(Pea,0,0,0), const(Pea,1,0,0), const(Pea,2,1,1), const(Pea,3,0,0), const(Pea,4,2,1) )
print("." * 45)

# Input Recipe Servings
Serv[0] = int(input("\nServings of Black Beans: "))
Serv[1] = int(input("Servings of Quinoa: "))
Serv[2] = int(input("Servings of Sona Masoori: "))
Serv[3] = int(input("Servings of Soybeans: "))
Serv[3] = int(input("Servings of Pinto Beans: "))
Serv[4] = int(input("Servings of Peas: "))
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
print("Price: ($" + str(round(price(Black,Serv[0]) + price(Quinoa,Serv[1]) + price(Masoori,Serv[2]) + price(Soy,Serv[3]) + price(Pinto,Serv[3]), 2)) + ")" )
print("Black Beans: ($" + str(price(Black, Serv[0])) + ")" )
print("Quinoa: ($" + str(price(Quinoa, Serv[1])) + ")" )
print("Masoori: ($" + str(price(Masoori, Serv[2])) + ")" )
print("Soybeans: ($" + str(price(Soy, Serv[3])) + ")" )
print("Pinto: ($" + str(price(Pinto, Serv[3])) + ")" )
print("Pea: ($" + str(price(Pea, Serv[4])) + ")" )
print("\n", "." * 45, "\n\n")
