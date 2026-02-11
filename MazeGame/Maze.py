"""
Name: Kevin Vo, Anthony Marcos
Date: 02/09/2026
Description:
This program allows a user to solve a maze loaded from a file. User starts at 's' and moves through maze until reaching 'f'.
"""

import check_input


def read_maze():
    """Reads a maze from file and stores it in 2D list. Each character (which also includes spaces) is stored as a separate element"""

    filename = input("Enter maze filename: ")
    maze = []

    with open(filename, "r") as file:
        for line in file:
            maze.append(list(line.rstrip("\n")))

    return maze


def find_start(maze):
    """Finds starting position s in the maze."""

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 's':
                return [row, col]



def display_maze(maze, loc):
    """Displays maze to screen, shows an X at user's current location"""

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if row == loc[0] and col == loc[1]:
                print("X", end="")
            else:
                print(maze[row][col], end="")
        print()


def main():
    """Main program loop for maze solver"""
    maze = read_maze()
    location = find_start(maze)

    print("\n-Maze Solver-")

    while True:
        display_maze(maze, location)

        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")

        choice = check_input.get_int_range("Enter choice: ", 1, 4)

        # Calculate new position
        new_row, new_col = location[0], location[1]

        if choice == 1:  # North
            new_row -= 1
        elif choice == 2:  # South
            new_row += 1
        elif choice == 3:  # East
            new_col += 1
        elif choice == 4:  # West
            new_col -= 1

        # Check wall
        if maze[new_row][new_col] == '*':
            print("You cannot move there.")
            continue

        # Move player
        location[0] = new_row
        location[1] = new_col

        # Check finish
        if maze[new_row][new_col] == 'f':
            display_maze(maze, location)
            print("Congratulations! You solved the maze.")
            break


main()

