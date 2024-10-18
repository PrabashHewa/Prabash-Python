class Team:
    def __init__(self, name, matches, points, rating):
        self.name = name
        self.matches = matches
        self.points = points
        self.rating = rating

    def update_rating(self):
        # Update the rating as points divided by matches
        self.rating = self.points / self.matches

def calculate_new_ratings(team_a, team_b, result):
    """
    Update the ratings based on the result.
    
    :param team_a: The stronger team (Team object)
    :param team_b: The weaker team (Team object)
    :param result: The result of the match. Options are:
                   'a_win' for Team A wins, 'b_win' for Team B wins, 'tie' for a tie.
    :return: Updated ratings for both teams.
    """
    rating_gap = abs(team_a.rating - team_b.rating)

    # Case 1: Rating gap < 40 points
    if rating_gap < 40:
        if result == 'a_win':
            team_a.points += team_b.rating + 50
            team_b.points += team_a.rating - 50
        elif result == 'b_win':
            team_a.points += team_b.rating - 50
            team_b.points += team_a.rating + 50
        elif result == 'tie':
            team_a.points += team_b.rating
            team_b.points += team_a.rating
    
    # Case 2: Rating gap >= 40 points
    else:
        if team_a.rating > team_b.rating:  # Team A is stronger
            if result == 'a_win':
                team_a.points += team_a.rating + 10
                team_b.points += team_b.rating - 10
            elif result == 'b_win':
                team_a.points += team_a.rating - 90
                team_b.points += team_b.rating + 90
            elif result == 'tie':
                team_a.points += team_a.rating - 40
                team_b.points += team_b.rating + 40
        else:  # Team B is stronger
            if result == 'a_win':
                team_a.points += team_a.rating + 90
                team_b.points += team_b.rating - 90
            elif result == 'b_win':
                team_a.points += team_a.rating - 10
                team_b.points += team_b.rating + 10
            elif result == 'tie':
                team_a.points += team_a.rating + 40
                team_b.points += team_b.rating - 40

    # Update matches count and new ratings
    team_a.matches += 1
    team_b.matches += 1
    team_a.update_rating()
    team_b.update_rating()

def main():
    # Get input from the user for Team A and Team B
    name_a = input("Enter Team A name: ")
    matches_a = int(input(f"Enter {name_a}'s matches played: "))
    points_a = int(input(f"Enter {name_a}'s total points: "))
    rating_a = float(input(f"Enter {name_a}'s rating: "))

    name_b = input("Enter Team B name: ")
    matches_b = int(input(f"Enter {name_b}'s matches played: "))
    points_b = int(input(f"Enter {name_b}'s total points: "))
    rating_b = float(input(f"Enter {name_b}'s rating: "))

    # Create Team objects
    team_a = Team(name=name_a, matches=matches_a, points=points_a, rating=rating_a)
    team_b = Team(name=name_b, matches=matches_b, points=points_b, rating=rating_b)

    # Get match result input
    result = input("Enter result ('a_win' for Team A wins, 'b_win' for Team B wins, 'tie' for a tie): ")

    # Calculate new ratings based on the match result
    calculate_new_ratings(team_a, team_b, result)

    # Print the updated ratings for both teams
    print(f"\nNew {team_a.name} rating: {team_a.rating:.2f}")
    print(f"New {team_b.name} rating: {team_b.rating:.2f}")
    print(f"\nNew {team_a.name} rating: {team_a.points:.2f}")
    print(f"New {team_b.name} rating: {team_b.points:.2f}")

if __name__ == "__main__":
    main()
