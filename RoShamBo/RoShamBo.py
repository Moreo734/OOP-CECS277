#Anthony Marcos
#This is the RockPaperScissors Game that I made
import check_input
import random

def weapon_menu():
    """This function will let the user select their weapon
        It asks the user to make a valid input and does not exit out until
        a valid input is entered.
    """
    while True:
        user_weapon = input("""Choose your Weapon: 
        R.Rock
        P.Paper
        S.Scissors
        B.Back
        """).strip().upper()
        if user_weapon in ("R", "P", "S", "B"):
            return user_weapon
        else: print("Invalid input. Please enter something else.")

def comp_menu():
    """This function will decide the weapon that the computer will have
        It creates a list of R,P,S and a randon number between 0 and the length of the list.
        From there it returns either R or P or S based on the comp random number.
    """
    wep_list = ["R", "P", "S"]
    rand_num = random.randint(0, len(wep_list) - 1)
    return wep_list[rand_num]


def find_winner(p_wep, c_wep):
    """This function will decide whether the computer or the human won by comparing weapons
       The Dictionary I created does most of the work here. It also returns 0, 1 ,2.
       This is done to tell the main function whether it is a winner, loser, or tie rather
       than just printing it.
       The weapons of both the Computer and User are passed into this function
    """
    weapon_logic = {
        "R": "S",
        "P": "R",
        "S": "P"
    }
    print("You Chose: ", p_wep)
    print("Computer Chose: ", c_wep)
    if p_wep == c_wep:
        return "Tie Nobody Wins", 0
    elif weapon_logic[p_wep] == c_wep:
        return "You Win!", 1
    else:
        return "You Lose! Computer Wins!", 2



def display_scores(p_score, c_score):
    """This function will display the score of both the human and computer
       All this does is print out the passed variables
    """
    print("User Score: ", p_score)
    print("Computer Score: ", c_score)

def main():
    """
    This is the main function. It calls upon the other functions as needed. This is
    where the user score weapons and comp counterpart are stored.
    It is all ran under a while loop that ends when the number 3 is input

    """
    menu_int = 0
    user_score = 0
    comp_score = 0
    while menu_int != 3:
        #This is the main work. This function is the whole game
        menu_int = check_input.get_int_range(""" RPS Menu:
        1. Play game
        2. Show Score
        3. Quit
        """,
        low = 1,
        high =3)
        #If 1 is selected it will proceed with the game as normal
        if menu_int == 1:
            user_weapon = weapon_menu()
            if user_weapon != "B":
                comp_weapon = comp_menu()
                result_str, win_num = find_winner(user_weapon, comp_weapon)
                print(result_str)
                if win_num == 1:
                    user_score += 1
                elif win_num == 2:
                    comp_score += 1
        #If number is 2 then it will display the score
        elif menu_int == 2:
            display_scores(user_score, comp_score)
        #If the number 3 is input it will do one last print statement and function call before exiting
        elif menu_int == 3:
            print("Final Score: ")
            display_scores(user_score, comp_score)
main()
