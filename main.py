#Anthony Marcos
#Gerald Stanfill
import random
import check_input

shellNum = random.randint(1,3)
wallet = 100
isRunning = True
guessNum = 1
bet = 0
#strings of all the ball possibilities along with a dictionary for them
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
 /     \ /     \ /  o  \
 ------- ------- -------
"""
shells = {
    1: shell_1,
    2: shell_2,
    3: shell_3
}

print("--Shell Game --")
print("Find the ball to double your bet amount!")

#loop here is the entirety of the game. Everytime the game ends it will start over from here
while isRunning and wallet > 0:
    print("\nYou have $" + str(wallet) + ".")
    bet = check_input.get_int_range("How much would you like to bet?", 1, int(wallet))

    print(r"""
   ___     ___     ___
  /   \   /   \   /   \
 /  1  \ /  2  \ /  3  \
 ------- ------- -------
""")

    guessNum = check_input.get_int_range("Make a guess:", 1, 3)
    print(shells[shellNum])
    #this if else statement determines whether the user guessed correctly or not
    # it also deals with removing and adding money to the wallet
    if guessNum == shellNum:
        print("Congratulations! You won!")
        wallet += bet
    else:
        print("Sorry, you lost!")
        wallet -= bet
    shellNum = random.randint(1,3)
    #final checks to see if the player has money and if they desire to play again
    if wallet == 0:
        print("You're out of money! Game Over!")
        break


    isRunning = check_input.get_yes_no("Do you want to play again? (Y/N) : ")
