from League import League

names = []
while True: #User inputs the names for the league
    name = input("Enter names for the teams: |do you want to stop? y=yes")
    if name == "y":
        break
    names.append(name)


my_league = League(names)
my_league.print()