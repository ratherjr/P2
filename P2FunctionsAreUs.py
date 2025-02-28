# Joseph Rather
'''Store women's soccer game stores and output them with the season record
In the dictionary you should store your team name, your team score, the opponent 
team name, the opponent team score, and whether it was a W or L for your team.'''

# Import Random and set min and max goals and 0 variables
import random
iGoalMax = 7
iGoalMin = 0
iWins = 0
iLosses = 0

def display_menu():
    iOption = 0
    while not iOption == 4 :
        print( """Select Option
Option 1- Select 2 Teams
Option 2- Generate random scores for both teams
Option 3- Display final record for a team
Option 4- Quit""")
        iOption = int( input( "Option: "))

        if iOption == 1 :
            teams()
        
        elif iOption == 2 :
            # function 4

        elif iOption == 3 :
            # enter function 5 here

        elif iOption == 4:
            print( "\nExiting the program. Goodbye!")    
    
        else : print("Please enter valid number character: ")


# Input home team name and number of games
sTeam = input("\nEnter your team name: ")
iNumGames = int( input( "Enter number of games in season: "))

# create dictionary and list for later use
dictGames = {}
lstStats = []

# For loop asking for info from each game the team played
for iCountGames in range(0,iNumGames):
    
    #gather inputs from games
    sOpponentTeam = input (f"\nEnter opponent team name for game {iCountGames + 1}: ")
    
    # reset team scores
    iYourScore = 0
    iOpponentScore = 0
    
    while (iYourScore == iOpponentScore):
        iYourScore = random.randrange(iGoalMin,iGoalMax)
        iOpponentScore = random.randrange(iGoalMin,iGoalMax)

    # find out if game was a win or a loss and store to variable
    if iYourScore > iOpponentScore :
        sWL = "W"
        iWins += 1
    else:
        sWL = "L"
        iLosses += 1

    # store all variables to list within dictionary
    lstStats = [sOpponentTeam, iYourScore, iOpponentScore, sWL]
    dictGames[iCountGames] = lstStats

# Output everything from dictionary and final record
print("\n\n\n\n\nFinal Results from this season:")
for iCountGames in range(0,len(dictGames)):
    lstGameStats = dictGames[iCountGames]
    print(f"\n{sTeam} vs. {lstGameStats[0]}")
    if lstGameStats[1] > lstGameStats[2] :
        print(f"Won {lstGameStats[1]} - {lstGameStats[2]}")
    else:
        print(f"Lost {lstGameStats[1]} - {lstGameStats[2]}")

print(f"\nEnding {sTeam} Record: {iWins} - {iLosses}")

# Calculate Win % and output remaining stuff
fWinPer = iWins / (iWins + iLosses) * 100
if fWinPer >= 75 :
    print(f"Win Percentage: {fWinPer:.1f}%")
    print(f"\nYou're going to the Women's Soccer National Tournament!!!!\n")
elif fWinPer >= 50 :
    print(f"Win Percentage: {fWinPer:.1f}%")
    print(f"\nYou had a pretty good season!\n")
else: 
    print(f"Win Percentage: {fWinPer:.1f}%")
    print(f"\nThis season wasn't that great :(")
    print(f"Try again next year.\n")

display_menu()