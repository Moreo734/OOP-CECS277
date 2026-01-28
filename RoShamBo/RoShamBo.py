import check_input
import random

def weapon_menu():
    #This function will let the user select their weapon
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
    #This function will decide the weapon that the computer will have
    wep_list = ["R", "P", "S"]
    rand_num = random.randint(0, len(wep_list) - 1)
    return wep_list[rand_num]


def find_winner(p_wep, c_wep):
    #This function will decide whether the computer or the human won by comparing weapons
    weapons = ("R", "P", "S")
    weapon_logic = {
        "R": "S",
        "P": "R",
        "S": "P"
    }
    if p_wep == c_wep:
        return "Tie Nobody Wins", 0
    elif weapon_logic[p_wep] == c_wep:
        return "You Win!", 1
    else:
        return "You Lose! Computer Wins!", 2



def display_scores(p_score, c_score):
    #This function will display the score of both the human and computer
    print("User Score: ", p_score)
    print("Computer Score: ", c_score)

def main():
    #This is the main function. It will call all of the previous functions
    menu_int = 0
    user_weapon = ""
    comp_weapon = ""
    user_score = 0
    comp_score = 0
    print("blank")
    while menu_int != 3:
        menu_int = check_input.get_int_range(""" RPS Menu:
        1. Play game
        2. Show Score
        3. Quit
        """,
        low = 1,
        high =3)

        if menu_int == 1:
            user_weapon = weapon_menu()
            if user_weapon != "B":
                comp_weapon = comp_menu()
                result_str, win_num = find_winner(user_weapon, comp_weapon)
                print(result_str)
                #print(win_num)
                if win_num == 1:
                    user_score += 1
                    #print(user_score)
                elif win_num == 2:
                    comp_score += 1

        elif menu_int == 2:
            display_scores(user_score, comp_score)
main()
