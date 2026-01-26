import check_input

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
    print("blank")

def find_winner(p_wep, c_wep):
    #This function will decide whether the computer or the human won by comparing weapons
    print("blank")

def display_scores(p_score, c_score):
    #This function will display the score of both the human and computer
    print("blank")

def main():
    #This is the main function. It will call all of the previous functions
    menu_int = 0
    print("blank")
    while menu_int != 3:
        user_weapon = ""
        comp_weapon = ""
        user_score = 0
        comp_score = 0
        print(""" RPS Menu:
        1. Play game
        2. Show Score
        3. Quit
        """)
        menu_int = check_input.get_int_range( low = 1, high =3)
        if menu_int == 1:
            weapon_menu()
            comp_menu()
            find_winner()

        if menu_int == 2:
            display_scores()
main()
