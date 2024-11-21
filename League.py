from Team import Team

class League:

    def __init__(self,teams):
        """
        constructor for league that copies the names of the teams into the list of objects of teams
        :param teams: list of names of teams
        """
        self.teams = []
        for _ in teams:
            self.teams.append(Team())
        i=0
        for team in self.teams:
            team.set_name(teams[i])
            i+=1


    def bool_game(self,points1,group1,points2,group2):
        for team in self.teams:
            if group1 not in self.teams or group2 not in self.teams:
                return False
        group1.game(points1,points2)
        group2.game(points2,points1)
        return True

    def print(self):
        for team in self.teams:
            team.print_team()
