class Team:

    def __init__(self):
        """
        default constructor
        """
        self.name = ""
        self.good_points = 0
        self.bad_points = 0
        self.win = 0
        self.lose = 0
        self.draw = 0

    def set_name(self, name):
        """
        changes the name of the team
        :param name: name
        :return: none
        """
        self.name = name

    def get_name(self):
        """
        returns the name of the team
        :return: name of team
        """
        return self.name

    def game(self,good,bad):
        """
        updates the goals of team after a game
        :param good: good_points
        :param bad: bad_points
        :return: none
        """
        self.good_points+=good
        self.bad_points+=bad


        if good > bad:
            self.win+=1
        elif bad > good:
            self.lose+=1
        elif bad == good:
            self.draw +=1

    def points(self):
        """
        will tell you how many points the team has
        :return: points of the team
        """
        return self.draw+3*self.win

    def print_team(self):
        """
        prints all the information of the team
        :return:
        """
        print(f"name:{self.name}|good points:{self.good_points}bad points:{self.bad_points}wins:{self.win}losses:{self.lose}draws:{self.draw}number of games:{self.lose + self.win + self.draw}number of points:{self.points()}")

