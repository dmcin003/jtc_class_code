# STRINGS have text in them
# String are surrounded by quotes

# assign a string variable
street = "Amsterdam Avenue"
#print(street)

# lyrics, using escape characters
lyrics = 'At first I was afraid, I was petrified, Kept thinking I could never \
live without you by my side, But then I spent so many nights thinking how you \
did me wrong, And I grew strong'
#print(lyrics)

# 'newline character' \n
lyrics = 'At first I was afraid, I was petrified, \nKept thinking I could never \
live without you by my side, \nBut then I spent so many nights thinking how you \
did me wrong, \nAnd I grew strong'
#print(lyrics)

# 'tab character' \t
lyrics = 'At first I was afraid, I was petrified, \nKept thinking I could never \
live without you by my side, \n\n\n\n\n\tBut then I spent so many nights thinking how you \
did me wrong, \n\t\tAnd I grew strong'
#print(lyrics)

# Formatted string / f-string
# set an integer variable called profit
profit = 120
my_f_string = f"The profit today is {profit*1000}"
#print(my_f_string)

# Putting two strings together
# make 2 strings
fruit1 = 'apple'
fruit2 = 'banana'

# concatenate the strings
fruit3 = fruit2 + ' ' + fruit1 + ' ' + 'orange'
#print(fruit3)


# making uppercase
#print(fruit3.upper())

# strings can have numbers
my_string2 = '2'
#print(type(my_string2))


## BOOLEAN VARIABLES
my_bool = True
my_bool2 = False

print(my_bool)
