
import random
import check_input
from check_input import get_int_range

shellNum = random.randint(1,3)
wallet = 100
isRunning = True
guessNum = 1
bet = 0

shell_1 = r"""
   ___     ___     ___
  /   \   /   \   /   \
 /  o  \ /     \ /     \
 ------- ------- -------
"""
shell_2= r"""
   ___     ___     ___
  /   \   /   \   /   \
 /     \ /  o  \ /     \
 ------- ------- -------
"""
shell_3= r"""
   ___     ___     ___
  /   \   /   \   /   \
 /     \ /     \ /  0  \
 ------- ------- -------
"""
shells = {
    1: shell_1,
    2: shell_2,
    3: shell_3
}

print("--Shell Game --")
print("Find the ball to double your bet amount!")

##loop will start around here
while isRunning and wallet > 0:
    print("\nYou have $" + str(wallet) + ".")
    bet = check_input.get_int_range("How much would you like to bet?", 0, int(wallet))

    print(r"""
   ___     ___     ___
  /   \   /   \   /   \
 /  1  \ /  2  \ /  3  \
 ------- ------- -------
""")

    guessNum = check_input.get_int_range("Make a guess:", 1, 3)
    print(shells[shellNum])
    if guessNum == shellNum:
        print("Congratulations! You won!")
        wallet += bet*2
    else:
        print("Sorry, you lost!")
        wallet -= bet
    shellNum = random.randint(1,3)
if wallet == 0:
    print("You're out of money! Game Over!")
isRunning = check_input.get_yes_no("Do you want to play again? (Y/N) : ")
