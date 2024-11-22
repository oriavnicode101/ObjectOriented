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
        """
        updates the status of both teams depending on the result of the game
        :param points1: points for the first team
        :param group1: team 1
        :param points2: points for the second team
        :param group2: team 2
        :return: true if the names of the teams are listed in the League
        """
        team_dict = {team.get_name(): team for team in self.teams}

        # Check if both teams exist
        if group1 not in team_dict or group2 not in team_dict:
            return False

        # Update both teams' statistics
        team_dict[group1].game(points1, points2)
        team_dict[group2].game(points2, points1)

        return True


    def print(self):
        """
        prints the table of the League
        :return:
        """
        for team in self.teams:
            team.print_team()
