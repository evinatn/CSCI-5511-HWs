import random
import itertools

num_players = 13
num_weeks = 13
players = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

# Function to generate a random league schedule
def generate_random_schedule():
    schedule = []

    for week in range(num_weeks):
        bye_player = players[week%num_players]  #one player out of the game every week
        other_players = [p for p in players if p!= bye_player]  #list of 12 players
        random.shuffle(other_players)  
         
        games = []
        for i in range(0,len(other_players),4):  #creating groups of 4
            game = other_players[i:i+4]
            games.append(game) 

        schedule.append(games) #game schedule for the week
    
    return schedule


# Function to count player matches in a schedule
def count_player_matches(schedule):
    player_counts = {}
    #loop through each player
    for player in players:
        #empty dictionary to store match counts for opponents
        opponent_counts = {}
        
        #loop through each opponent (excluding the current player)
        for opponent in players:
            if opponent != player:
                opponent_counts[opponent]=0
        #add the opponent counts dictionary to the player's entry in the player_counts dictionary
        player_counts[player] = opponent_counts
    
    for week_games in schedule:
        for game in week_games:
            for player1, player2 in itertools.combinations(game, 2):  #goes through all possible combinations of 2 players so all of it will be counted only once
                #increases match count for both players
                player_counts[player1][player2] += 1
                player_counts[player2][player1] += 1
    
    return player_counts

# Function to evaluate a schedule's fairness score
def evaluate_schedule(schedule):
    player_counts = count_player_matches(schedule)
    fairness_score = 0
    for player1 in players:
        for player2 in players:
            if player1 != player2: 
                fairness_score += abs(player_counts[player1][player2] - 1)
    
    return fairness_score

# Function to perform hill climbing optimization
def hill_climbing(iterations):
    best_schedule = generate_random_schedule()
    best_score = evaluate_schedule(best_schedule)
    
    for _ in range(iterations):
        next_schedule = generate_random_schedule()
        next_score = evaluate_schedule(next_schedule)
        
        if next_score < best_score:
            best_schedule = next_schedule
            best_score = next_score
    
    return best_schedule, best_score 

# Function to perform simulated annealing optimization
def simulated_annealing(iterations, initial_temperature, cooling_rate):
    current_schedule = generate_random_schedule()
    current_score = evaluate_schedule(current_schedule)
    best_schedule = current_schedule
    best_score = current_score
    
    for i in range(iterations):
        next_schedule = generate_random_schedule()
        next_score = evaluate_schedule(next_schedule)
        
        temperature = initial_temperature * (1-i/iterations)
        delta_E = current_score-next_score
        acceptance_probability = min(1,(delta_E)/temperature)
        
        if random.random() < acceptance_probability:
            current_schedule = next_schedule
            current_score = next_score
        
        if current_score < best_score:
            best_schedule = current_schedule
            best_score = current_score
    
    return best_schedule, best_score 

# Generate the schedule
schedule = generate_random_schedule()

# Run hill climbing and print results
best_schedule_hill, best_score_hill = hill_climbing(10000)
print("\nHill Climbing Results:")
print("Best Schedule:")
for i, games in enumerate(best_schedule_hill):
    print('Bye for Player', players[i] + ':', end=' ')
    for game in games:
        print(game, end=' ')
    print()

player_matches_hill = count_player_matches(best_schedule_hill)
print("\nReplay Summary")
for player, matches in player_matches_hill.items():
    formatted_matches = [] 
    for opponent, count in matches.items():
        formatted_string = opponent + ':' + str(count) 
        formatted_matches.append(formatted_string)
    formatted_str = player + ': ' + ', '.join(formatted_matches)
    print(formatted_str)

# Run simulated annealing and print results
best_schedule_sa, best_score_sa = simulated_annealing(10000, 10.0, 0.001)
print("\nSimulated Annealing Results:")
print("Best Schedule:")
for i, games in enumerate(best_schedule_sa):
    print('Bye for Player', players[i] + ':', end=' ')
    for game in games:
        print(game, end=' ')
    print()
    
player_matches_sa = count_player_matches(best_schedule_sa)
print("\nReplay Summary")
for player, matches in player_matches_sa.items():
    formatted_matches = [] 
    for opponent, count in matches.items():
        formatted_string = opponent + ':' + str(count) 
        formatted_matches.append(formatted_string)
    formatted_str = player + ': ' + ', '.join(formatted_matches)
    print(formatted_str)
