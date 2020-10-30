'''
Planning challenge 2!

For each piece here, write out the pseudocode as comments FIRST, then write your code!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should be a dictionary that has 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

#initialize 3 dictionaries as orders
order_1 = {'destination':'Sunrise','date_shipped':'10/29/2020','weight':.7}
order_2 = {'destination':'Bronx','date_shipped':'10/28/2020','weight':2.7}
order_3 = {'destination':'Monrovia','date_shipped':'10/27/2020','weight':1.7}

print(order_1)
print(order_2)
print(order_3)


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are storedin 1 variable). 

Your database can either be a dictionary or a list. 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')
# initialize and add orders to database
database = [order_1,order_2,order_3]
print(database)

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

def add_order(order,database):
	#add order to the list
	database.append(order)

order_4 = {'destination':'Queens','date_shipped':'10/26/2020','weight':11.7}
add_order(order_4,database)
print(database)
'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means that it should add a new key/value pair called 'complete' to a specific order, and set the value to True

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')

def complete_order(order,database):
	#loop through database
	for item in database:
		#if order == item in the database
		if order == item:
			# add key value pair called complete and set it to true
			order['complete'] = True
	

complete_order(order_4,database)
print(database)

