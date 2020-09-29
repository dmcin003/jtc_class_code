print("Challenge 3.1: Debug code snippets")

print()

print("Code Snippet 1:")

a = 1
b = 1
c = (a > b)

print("The value of c is False since a is equal to b.")

print()

print("Code Snippet 2:")

d = (True or (5 > 7) or not (8 < 20))

print("The value of d is True since there is a True boolean data type at the begining of the first or operator and the whole expression consist of only or and not operators.")

print()


print("Code Snippet 3:")

m = "GOAT"
n = "goat"

o = (m == n)

print ("The value of o is False since Python is case-sensitive.")

print()

print("Code Snippet 4:")

u = 5
v = 2

if u * v == 10:
    print("The product of a and b is 10")
else:
    print("The product of a and b is not 10")

print()

print("Code Snippet 5:")
x = 15
y = 25

z = 30

if z < x:
    print("z is less than x")

elif z > x and z < y:
    print("z is between x and y")

else:
    print("z is greater than y")


print()
print()
print()

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Creating variables")
# Create variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
facebook = 250
google = 1400
microsoft = 200
print()


print("Challenge 3.2.2: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What is your name? ")
# TODO: Write code to ask the client his savings and save it to another variable.
savings = input("What is your savings amount? Please enter the numerical amount. example: 700 or 700.50: ")
savings_is_float = savings.replace(".","",1).isdigit()

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.3: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
#checks to make sure the user enters a number and not anything else.
if savings.isdigit() == True or savings_is_float:
	#convert savings entered into a float to use in calculations
	float_savings = float(savings)

	if float_savings>=0:
		#perform calculations and assigns info to the choosen stock's variables to be printed out.
		if stock == "amzn":
			shares = float_savings/amazon
			stock_choosen = "Amazon"
			stock_price = amazon
		elif stock == "aapl":
			shares = float_savings/apple
			stock_choosen = "Apple"
			stock_price = apple
		elif stock == "fb":
			shares = float_savings/facebook
			stock_choosen = "Facebook"
			stock_price = facebook
		elif stock == "goog":
			shares = float_savings/google
			stock_choosen = "Google"
			stock_price = google
		elif stock == "msft":
			shares = float_savings/microsoft
			stock_choosen = "Microsoft"
			stock_price = microsoft
		else:
			print("Please enter a valid stock")
	else:
		print("Insufficient funds!")
else:
	print("Please enter a valid number for the savings amount!")



print()

print("Challenge 3.2.4: Output for the user the result")
# checks if the user entered the savings and  the stock correctly 
if (savings.isdigit() == True or savings_is_float) and (stock=="amzn" or stock=="aapl" or stock=="fb" or stock=="goog" or stock=="msft"):
	# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
	# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
	print(f"{name} has ${savings} in savings and can buy {shares} shares of {stock_choosen} at the current price of {stock_price}")
else:
	pass

print()