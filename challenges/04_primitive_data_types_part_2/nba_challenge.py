print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Jamal Murray made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Jamal Murray made {james_harden_3pts_made} 3 point shots")

print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_shot_attempts = 93
fred_vanvleet_3pts_shot_attempts = 110
james_harden_3pts_shot_attempts = 109
print()

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and attempted {jamal_murray_3pts_shot_attempts} 3 point shots.")
print(f"In the 2020 NBA playoffs, Jamal Murray made {fred_vanvleet_3pts_made} 3 point shots and attempted {fred_vanvleet_3pts_shot_attempts} 3 point shots.")
print(f"In the 2020 NBA playoffs, Jamal Murray made {james_harden_3pts_made} 3 point shots and attempted {james_harden_3pts_shot_attempts} 3 point shots.")


print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
#stores the 3 players percentages as real percentile values
jamal_murray_3pts_percentage= (jamal_murray_3pts_made/jamal_murray_3pts_shot_attempts)*100
fred_vanvleet_3pts_percentage= (fred_vanvleet_3pts_made/fred_vanvleet_3pts_shot_attempts)*100
james_harden_3pts_percentage= (james_harden_3pts_made/james_harden_3pts_shot_attempts)*100
print(f"Jamal Murray's 3 point percentage is {jamal_murray_3pts_percentage}")
print(f"Fred VanVleet's 3 point percentage is {fred_vanvleet_3pts_percentage}")
print(f"James Harden's 3 point percentage is {james_harden_3pts_percentage}")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
text ="The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\n They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\n Those three have made good developments with the Pelicans, especially Brandon Ingram.\n But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\n Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\n The Lakers ended the season atop the Western Conference with a record of 49-14.\n They were narrowly behind the Bucks for the best record in the league.\n Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\n Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(text)  

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print(text.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_best = False
print(f"The lakers are the best team is {lakers_are_best}")


print('Challenge 3.4: Type Conversion')
lakers_are_best_int = int(lakers_are_best)
print(lakers_are_best_int)
lakers_are_best_float = float(lakers_are_best)
print(lakers_are_best_float) 

print('Challenge 3.5: Type Conversion Part 2')
print(str(jamal_murray_3pts_percentage))
print(str(fred_vanvleet_3pts_percentage))
print(str(james_harden_3pts_percentage))
print(int(jamal_murray_3pts_percentage))
print(int(fred_vanvleet_3pts_percentage))
print(int(james_harden_3pts_percentage))
