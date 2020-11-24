
import random

bars = ["The Hamilton", "1020 Bar", "The Heights", "The Dead Poet"]

people = ["Mattan","That person you forgot to text back","Glenn Hubbard","Samuel L. Jackson"]

random_bar = random.choice(bars)

random_person = random.choice(people)

print(f"How about you go to {random_bar} with {random_person}?")