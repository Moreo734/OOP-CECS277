
import random
import check_input
from check_input import get_int_range

shellNum = random.randint(1,3)
wallet = 100
sentinelCHar = "Y"


print("--Shell Game --")
print("Find the ball to double your bet amount!")

##loop will start around here
#while sentinelCHar == "Y":
print("\nYou have $" + str(wallet) + ".")
check_input.get_int_range("How much would you like to bet?", 0, int(wallet))

