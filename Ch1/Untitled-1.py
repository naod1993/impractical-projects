import random
import sys


print("\nWelcome to silly name generator")
print("\nWe will give you a good name for you sidekick")

first_names = ('a', 'b', 'c', 'd', 'e', 'f')
last_names = ('a', 'b', 'c', 'd', 'e', 'f')

while True:
    first = random.choice(first_names)
    last = random.choice(last_names)

    print("{}{}".format(first, last), file=sys.stderr)

    try_again = input("\nTry Again? Press Y for yes or N for no:")
    if try_again.lower() == "n":
        break

input("\nPress Enter key to exit.")



