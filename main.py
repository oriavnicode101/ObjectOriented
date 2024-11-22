from League import League


names = []

while True:    #User inputs the names for the league
    name = input("Enter names for the teams: |do you want to stop? y=yes")
    if name == "y":
        break
    names.append(name)

my_league = League(names) # creates a new League object using the constructor

while True:

    Team1 = input("Enter the name of the first team to play:")
    Team2 = input("Enter the name of the second team to play:")
    points1 = int(input("Enter the amount of goals the first team scored:"))
    points2 = int(input("Enter the amount of goals the second team scored:"))

    result = my_league.bool_game(group1 = Team1,group2 = Team2,points1=points1,points2=points2)

    if result:
        print("game recorded!")
    else:
        print("wrong teams names try again")
        continue

    my_league.print()

    condition = input("Do you want to stop? | y=yes")
    if condition == "y":
        break