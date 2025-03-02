# Joseph Rather, Chad Laursen, Alayna Smith, Elias Fobert, Isaac Johnson
'''Store women's soccer game scores and output them with the season record
In the dictionary you should store your team name, your team score, the opponent 
team name, the opponent team score, and whether it was a W or L for your team.'''

# Based on the instructions it looks like we can make one big function that includes some of the other functions
# This means that we need to make the five functions first and then the 6th function will be the big one that includes some of them

# FUNCTION #1 - Chad
def display_intro():
    print("Welcome to the Women's Soccer Season Simulation!")
    print("In this simulation, you'll enter your team name and the opponents.")
    print("Scores will be randomly generated, and you'll receive your season results at the end.")
    player_name = input("Please enter your name: ")
    return player_name

# FUNCTION #2 - Isaac
def Menu():
    print("Menu")
    print("1. Play Another Game")
    print("2. View Season record")
    print("3.  Exit")
    return int(input("Enter your choice (1, 2, or 3): "))

# FUNCTION #3 - Joseph

def teams(lstTeams=["BYU","Utah","UVU","USU","Utah Tech","SLCC"]):
    iCount = 0
    global sTeam
    if sTeam == None:
        for team in lstTeams:
            iCount += 1
            print(f"{iCount}. {team}")

        iHomeTeam = int(input("Enter the number of the home team: "))
        print(f'\n')
        
        sTeam = lstTeams[iHomeTeam - 1]

        del lstTeams[iHomeTeam - 1]
    
    iCount = 0
    for team in lstTeams:
        iCount += 1
        print(f"{iCount}. {team}")

    iAwayTeam = int(input("Enter the number of the away team: "))
    sAwayTeam = lstTeams[iAwayTeam - 1]

    print(f'\n')
    return sAwayTeam

# FUNCTION #4 - Alayna
import random

def play_game(sTeam, sAwayTeam):
    print(f"Game between {sTeam} and {sAwayTeam}")
    homeScore, opponentScore = 0, 0
    while homeScore == opponentScore:
        homeScore = random.randint(0,7)
        opponentScore = random.randint(0,7)
    if homeScore > opponentScore:
        result = "W"
    else:
        result = "L"
    return homeScore, opponentScore, result

# FUNCTION #5 - Elias
def final_record(sTeam, iWins, iLosses, fWinPer):
    print(f"{sTeam} Season Final Record")
    print(f"Ending Team Record: wins: {iWins} - losses: {iLosses}")
    fWinPer = (iWins / (iWins + iLosses)) * 100 if (iWins + iLosses) > 0 else 0
    return sTeam, iWins, iLosses, fWinPer
    

# FUNCTION #6 - the main function
def Main():
    print("nothing")
    # Call the display_intro function to get player name
    player_name = display_intro()
    print(f"\nWelcome, {player_name}!")

# Import Random and set min and max goals and 0 variables
import random
iGoalMax = 7
iGoalMin = 0
iWins = 0
iLosses = 0
sTeam = None


Main()

Menu()

def display_menu():  # Ensure this is defined before calling it
    iOption = 0
    while iOption != 4:  # Fixed condition
        print( """Select Option
Option 1- Select 2 Teams
Option 2- Generate random scores for both teams
Option 3- Display final record for a team
Option 4- Quit""")
        iOption = int(input("Option: "))

        if iOption == 1:
            teams()  # Call teams to select two teams
        
        elif iOption == 2:
            # Make sure to define sOpponentTeam before using it.
            sOpponentTeam = teams()  # Call this to select the opponent team
            homeScore, opponentScore, result = play_game(sTeam, sOpponentTeam)  # Pass the teams to play_game
            if result == "W":
                iWins += 1
            else:
                iLosses += 1
            # Call final_record or other relevant function to display or process scores

        elif iOption == 3:
            # Call final_record function here
            final_record(sTeam, iWins, iLosses, fWinPer)  # Example function call

        elif iOption == 4:
            print("\nExiting the program. Goodbye!")    

        else:
            print("Please enter a valid number character: ")


# Input home team name and number of games
sTeam = input("\nEnter your team name: ")
iNumGames = int( input( "Enter number of games in season: "))

# create dictionary and list for later use
lstGames = ["BYU","Utah","UVU","USU","Utah Tech","SLCC"]
lstStats = []
dictGames = {}

# For loop asking for info from each game the team played
for iCountGames in range(0, iNumGames):
    
    # Call function #3
    sOpponentTeam = teams(lstGames)

    # reset team scores
    iYourScore = 0
    iOpponentScore = 0
    
    while (iYourScore == iOpponentScore):
        iYourScore = random.randrange(iGoalMin, iGoalMax)
        iOpponentScore = random.randrange(iGoalMin, iGoalMax)

    # find out if game was a win or a loss and store to variable
    if iYourScore > iOpponentScore:
        sWL = "W"
        iWins += 1
    else:
        sWL = "L"
        iLosses += 1

    # store all variables to list within dictionary
    lstStats = [sOpponentTeam, iYourScore, iOpponentScore, sWL]
    dictGames[iCountGames] = lstStats

# Output everything from dictionary and final record
print("\n\n\nFinal Results from this season:")
for iCountGames in range(0,len(dictGames)):

    lstGameStats = dictGames[iCountGames]
    print(f"\n{sTeam} vs. {lstGameStats[0]}")
    if lstGameStats[1] > lstGameStats[2]:
        print(f"Won {lstGameStats[1]} - {lstGameStats[2]}")
    else:
        print(f"Lost {lstGameStats[1]} - {lstGameStats[2]}")

print(f"\nEnding {sTeam} Record: {iWins} - {iLosses}")

# Calculate Win % and output remaining stuff
fWinPer = iWins / (iWins + iLosses) * 100
if fWinPer >= 75:
    print(f"Win Percentage: {fWinPer:.1f}%")
    print(f"\nYou're going to the Women's Soccer National Tournament!!!!\n")
elif fWinPer >= 50:
    print(f"Win Percentage: {fWinPer:.1f}%")
    print(f"\nYou had a pretty good season!\n")
else: 
    print(f"Win Percentage: {fWinPer:.1f}%")
    print(f"\nThis season wasn't that great :(")
    print(f"Try again next year.\n")

display_menu()