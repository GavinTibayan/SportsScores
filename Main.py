# Create an Intramural score tracker

# Each team entry is a list that includes
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against

# You will ask how many teams are playing.
TCheck = int(1)
while TCheck == 1:
    Teams = input("How many teams are playing?")
    if int(Teams) > int(1):
        TCheck -=1
        TLst = []
    else:
        print("Now a valid number of teams, please try again.")
# Loop that many times, create a team and set all scores to 0, then append it to your list of teams
print("What are the team names?")
while int(Teams) > 0:
    TLst.append([input(),0,0,0,0,0,0])
    print("Team:",TLst[-1])
    Teams = int(Teams) - int(1)
print(TLst)
Length = []
on = int(1)
for i in range(len(TLst)+1):
    Length.append(i)
Length.remove(0)
print(Length)
# Start an infinite loop for main menu
#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit
while on == 1:
    print("\nWhat would you like to do?:\n1) Add score\n2) See Team stats\n3) See Overall Standing\n4) Quit")
    num = input()
#   1) Enter team 1, team 2, goals for team 1, goals for team 2
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie
    if num == "1":
        TSCheck = 1
        while TSCheck == 1:
            print("What's your first team?")
            TS1 = int(input())
            if TS1 in Length:
                TSCheck = 2
                while TSCheck == 2:
                    print("What's your second team?")
                    TS2 = int(input())
                    if TS2 in Length and TS2 != TS1:
                        TSCheck = 3
                        #print("How many points did",TLst[TS1-1[0]],"Score?")
                        GFor1 = int(input())
                        #print("How many points did",TLst[TS2-1[0]],"Score?")
                        GFor2 = int(input())
                        if GFor1 > GFor2:
                            print("Team",TLst[TS1],"wins against",TLst[TS2],"by",GFor1,"-",GFor2)
                            TLst[TS1[2]] +=1
                            TLst[TS2[3]] +=1
                            TLst[TS1[5]] += GFor1
                            TLst[TS1[6]] += GFor2
                            TLst[TS2[5]] += GFor2
                            TLst[TS2[6]] += GFor1
                        elif GFor1 == GFor2:
                            print("Both team",TLst[TS1],"and",TLst[TS2],"tie by",GFor1,"-",GFor2)
                            TLst[TS1[4]] += 1
                            TLst[TS2[4]] += 1
                            TLst[TS1[5]] += GFor1
                            TLst[TS1[6]] += GFor2
                            TLst[TS2[5]] += GFor2
                            TLst[TS2[6]] += GFor1
                        else:
                            print("Team",TLst[TS2],"wins against",TLst[TS1],"by",GFor2,"-",GFor1)
                            TLst[TS1[3]] += 1
                            TLst[TS2[2]] += 1
                            TLst[TS1[5]] += GFor1
                            TLst[TS1[6]] += GFor2
                            TLst[TS2[5]] += GFor2
                            TLst[TS2[6]] += GFor1
                    else:
                        print("Team already chosen, pick a different team")

#   2) Print a list of team names.
#       Once the user selects, Print out their stats
    elif num == "2":
        TVCheck = 1
        while TVCheck == 1:
            print("What team would you like to view?")
            print("Team List:")
            for tl2 in range(len(TLst)):
                print(Length[tl2],"-",TLst[tl2])
            TV = int(input())
            if TV in Length:
                TVCheck -=1
                for o in range(int(TV)+1):
                    pass
                print(TLst[o-1])
            else:
                print("Not a valid team, please try again")
#   3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.
    elif num == "3":
        pass
#   4) Say goodbye and break out of the loop
    elif num == "4":
        on -=1
        print("\n\t\tGoodbye!")
    else:
        print("\n\tInvalid number, please try again\n")



