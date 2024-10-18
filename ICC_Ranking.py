class Team:
    def __init__(self, name, matches, points, rating):
        self.name = name
        self.matches = matches
        self.points = points
        self.rating = rating

def update_ranking_table(teams, team1_name, team2_name, series_results):
    team1 = next((team for team in teams if team.name == team1_name), None)
    team2 = next((team for team in teams if team.name == team2_name), None)
    
    if team1 is None or team2 is None:
        print("One of the teams is not in the ranking table.")
        return

    # Initialize series points
    team1_series_points = 0
    team2_series_points = 0
    number_of_matches = len(series_results)
    
    # Step 1: Calculate Series Points
    for result in series_results:
        if result.lower() == team1_name.lower():  # Team 1 wins
            team1_series_points += 1
        elif result.lower() == team2_name.lower():  # Team 2 wins
            team2_series_points += 1
        elif result.lower() == "draw":  # Draw
            team1_series_points += 0.5
            team2_series_points += 0.5

    # Awarding bonus points
    if team1_series_points > team2_series_points:
        team1_series_points += 1  # Team 1 wins the series
    elif team2_series_points > team1_series_points:
        team2_series_points += 1  # Team 2 wins the series
    else:
        team1_series_points += 0.5  # Series drawn
        team2_series_points += 0.5

    # Step 2: Calculate Ratings Points
    rating_gap = abs(team1.rating - team2.rating)

    if rating_gap < 40:  # Less than 40
        team1_rating_points = (team1_series_points * (team2.rating + 50)) + (team2_series_points * (team2.rating - 50))
        team2_rating_points = (team2_series_points * (team1.rating + 50)) + (team1_series_points * (team1.rating - 50))
    else:  # 40 or more
        if team1.rating > team2.rating:  # Team 1 is stronger
            team1_rating_points = (team1_series_points * (team1.rating + 10)) + (team2_series_points * (team1.rating - 90))
            team2_rating_points = (team2_series_points * (team2.rating + 90)) + (team1_series_points * (team2.rating - 10))
        else:  # Team 2 is stronger
            team2_rating_points = (team2_series_points * (team2.rating + 10)) + (team1_series_points * (team2.rating - 90))
            team1_rating_points = (team1_series_points * (team1.rating + 90)) + (team2_series_points * (team1.rating - 10))

    # Step 3: Update Team Rankings
    total_series_points = number_of_matches + 1  # Total matches played + 1 for the series winner
    team1.points += team1_rating_points
    team1.matches += total_series_points
    team2.points += team2_rating_points
    team2.matches += total_series_points

    # Update ratings
    team1.rating = team1.points / team1.matches
    team2.rating = team2.points / team2.matches

    # Sort teams by rating after updates
    teams.sort(key=lambda x: x.rating, reverse=True)

def print_ranking_table(teams):
    print(f"{'Team':<15}{'Matches':<10}{'Points':<10}{'Rating':<10}")
    for team in teams:
        print(f"{team.name:<15}{team.matches:<10}{team.points:<10}{team.rating:<10.2f}")

# Initial Rankings for the teams
teams = [
    Team("Australia", 30, 3715, 124.0),
    Team("India", 29, 3448, 119.0),
    Team("England", 38, 4111, 108.0),
    Team("South Africa", 21, 2179, 104.0),
    Team("Sri Lanka", 25, 2271, 91.0),
    Team("New Zealand", 25, 2220, 89.0),
    Team("West Indies", 26, 1992, 77.0),
    Team("Pakistan", 20, 1528, 76.0),
    Team("Bangladesh", 23, 1541, 67.0)
]

# Taking user input for the series
team1_name = input("Enter the name of Team 1: ")
team2_name = input("Enter the name of Team 2: ")
number_of_matches = int(input("Enter the number of matches in the series: "))

series_results = []
for i in range(number_of_matches):
    result = input(f"Enter the result of match {i + 1} (win/loss/draw) for {team1_name} vs {team2_name}: ")
    series_results.append(result)

# Update rankings and print the updated table
update_ranking_table(teams, team1_name, team2_name, series_results)
print("\nUpdated Ranking Table:")
print_ranking_table(teams)



