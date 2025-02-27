# Joseph Rather, Chad Laursen, Alayna Smith, Elias Fobert, Isaac Johnson
'''Store women's soccer game scores and output them with the season record
In the dictionary you should store your team name, your team score, the opponent 
team name, the opponent team score, and whether it was a W or L for your team.'''

# Based on the instructions it looks like we can make one big function that includes some of the other functions
# This means that we need to make the five functions first and then the 6th function will be the big one that includes some of them

# FUNCTION #1


# FUNCTION #2


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
    print(f'\n')
    return lstTeams[iAwayTeam - 1]

# FUNCTION #4


# FUNCTION #5


# FUNCTION #6 - the main function
def Main():
    null = None

# Import Random and set min and max goals and 0 variables
import random
iGoalMax = 7
iGoalMin = 0
iWins = 0
iLosses = 0
sTeam = None

# Input number of games
iNumGames = int( input( "\nEnter number of games in season: "))
print(f'\n')

# create dictionary and list for later use
lstGames = ["BYU","Utah","UVU","USU","Utah Tech","SLCC"]
lstStats = []
dictGames = {}

# For loop asking for info from each game the team played
for iCountGames in range(0,iNumGames):
    
    # Call function #3
    sOpponentTeam = teams(lstGames)

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
print("\n\n\nFinal Results from this season:")
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