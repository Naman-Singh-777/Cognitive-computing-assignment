# 1
print("Life is beautiful, enjoy every moment.")

# 2.1
my_age = 25
friends_age = 27
print(f"Our combined age is {my_age + friends_age}")

# 2.2
first_name = "John"
last_name = "Doe"
print(f"Hello, I'm {first_name + ' ' + last_name}")

# 2.3
cats = 3
print(f"I have {cats} lovely cats")

# 3.1
temperature = 25
if temperature > 0:
    print("It's warm outside.")
elif temperature < 0:
    print("Brrr, it's freezing!")
else:
    print("It's exactly freezing point")

# 3.2
pizza_slices = 7
print("I have " + ("an even" if pizza_slices % 2 == 0 else "an odd") + " number of pizza slices.")

# 4.1
print("Counting down to launch:")
for seconds in range(1, 11):
    print(seconds)
print("Blast off! 🚀")

# 4.2
energy = 1
while energy <= 10:
    print(f"Energy level: {energy}")
    energy += 1

# 4.3
savings = sum(range(1, 101))
print(f"If I save $1 more each day, I'll have ${savings} after 100 days")

# 5.1
friend_ages = [25, 30, 22, 28, 27]
print(f"Youngest friend is {min(friend_ages)}, oldest is {max(friend_ages)}")

# 5.2
my_pets = {"dog": "Buddy", "cat": "Luna", "fish": "Nemo"}
print(f"My dog's name is {my_pets['dog']}")

# 5.3
scores = [85, 92, 78, 95, 88]
print(f"Scores from highest to lowest: {sorted(scores, reverse=True)}")
print(f"Scores from lowest to highest: {sorted(scores)}")

# 5.4
morning_routine = {"wake_up": "7:00", "breakfast": "7:30"}
evening_routine = {"dinner": "19:00", "sleep": "23:00"}
daily_routine = {**morning_routine, **evening_routine}
print(f"My daily schedule: {daily_routine}")

# 6.1
message = "Hello, how are you today?"
vowel_count = sum(1 for letter in message.lower() if letter in 'aeiou')
print(f"That message had {vowel_count} vowels")

# 6.2
message = "Have a great day"
print(f"Your message backwards is: {message[::-1]}")

# 6.3
word = "racecar"
print("Yes, it's a palindrome!" if word == word[::-1] else "Nope, not a palindrome")

# 7.1
with open("diary.txt", "w") as diary:
    diary.write("Dear diary, today was amazing!")
with open("diary.txt", "r") as diary:
    print(diary.read())

# 7.2
with open("diary.txt", "a") as diary:
    diary.write("\nCan't wait for tomorrow!")
with open("diary.txt", "r") as diary:
    print(diary.read())

# 7.3
with open("diary.txt", "r") as diary:
    print(f"I wrote {len(diary.readlines())} lines in my diary today")

# 8.1
try:
    cookies = 10
    friends = 0
    print(f"Each friend gets {cookies/friends} cookies")
except ZeroDivisionError:
    print("Oh no! I don't have any friends to share cookies with 😢")

# 8.2
try:
    age = int(input("How old are you? "))
except ValueError:
    print("That's not a real age! 😅")

# 8.3
try:
    print(1/0)
except:
    print("Oops, something went wrong!")
finally:
    print("But life goes on! 😊")

# 9.1
from random import randint
lottery_numbers = [randint(1, 100) for _ in range(5)]
print(f"Today's lucky numbers are: {lottery_numbers}")

# 9.2
from random import randint
lucky_number = randint(1, 100)
is_prime = all(lucky_number % i != 0 for i in range(2, int(lucky_number**0.5) + 1))
print(f"My lucky number {lucky_number} is {'prime' if is_prime else 'not prime'}")

# 9.3
from random import randint
roll = randint(1, 6)
print(f"🎲 You rolled a {roll}!")

# 9.4
from random import shuffle
playlist = ["Jazz", "Rock", "Pop", "Classical", "Blues"]
shuffle(playlist)
print(f"Today's shuffle: {playlist}")

# 9.5
from random import choice
meals = ["Pizza", "Sushi", "Burger", "Salad"]
print(f"Tonight's dinner will be... {choice(meals)}!")

# 9.6
from random import choice
import string
password = ''.join(choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(10))
print(f"Your new password is: {password}")

# 9.7
from random import choice
suits = ['♥', '♦', '♣', '♠']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(f"Your card is: {choice(cards)}{choice(suits)}")

# 10.1
import sys
if len(sys.argv) > 2:
    shopping_items = int(sys.argv[1]) + int(sys.argv[2])
    print(f"You need to buy {shopping_items} items")

# 10.2
import sys
if len(sys.argv) > 1:
    message = sys.argv[1]
    print(f"Your message is {len(message)} characters long")

# 11.1
from math import sqrt
pizza_area = 16
print(f"Your pizza has a radius of {sqrt(pizza_area)} inches")

# 11.2
from datetime import datetime
print(f"Right now it's: {datetime.now().strftime('%I:%M %p on %A, %B %d, %Y')}")

# 11.3
import os
print("Files in my folder:", [f for f in os.listdir() if not f.startswith('.')])
