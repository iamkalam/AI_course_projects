import random


#probabilities 
outcomes = [0, 1, 2, 3, 4, 6, 'W']
probabilities = [30, 25, 15, 5, 12, 8, 5]  # Percentages
#helper fun 

def balloutcomee():
    return random.choices(outcomes, weights=probabilities, k=1)[0]


def create_batsmen():
    return {f"Batsman {i}": {"runs": 0, "balls": 0} for i in range(1, 12)}


def simulaledinnings(team_name):
    print(f"\n{'='*70}")
    print(f"{team_name} INNINGS".center(70))
    print("="*70)

    batsmen = create_batsmen()
    bowlers = {f"Bowler {i}": {"runs": 0, "wickets": 0, "overs": 0} for i in range(1, 6)}

    striker = 1
    non_striker = 2
    next_batsman = 3

    total_runs = 0
    wickets = 0
    fall_of_wickets = []
    runs_per_over = []

    ball_number = 0

    for over in range(20):
        if wickets == 10:
            break

        over_runs = 0
        bowler = f"Bowler {(over % 5) + 1}"

        for ball in range(6):
            if wickets == 10:
                break

            outcome = balloutcomee()
            ball_number += 1

            current_batsman = f"Batsman {striker}"
            batsmen[current_batsman]["balls"] += 1

            if outcome == 'W':
                wickets += 1
                bowlers[bowler]["wickets"] += 1
                fall_of_wickets.append(f"{total_runs}/{wickets} (Ball {ball_number})")
                striker = next_batsman
                next_batsman += 1
            else:
                total_runs += outcome
                over_runs += outcome
                batsmen[current_batsman]["runs"] += outcome
                bowlers[bowler]["runs"] += outcome

                if outcome % 2 == 1:
                    striker, non_striker = non_striker, striker

        runs_per_over.append(over_runs)
        bowlers[bowler]["overs"] += 1
        striker, non_striker = non_striker, striker

    overs_played = ball_number / 6
    run_rate = total_runs / overs_played if overs_played > 0 else 0

    return {
        "team": team_name,
        "total": total_runs,
        "wickets": wickets,
        "overs": overs_played,
        "run_rate": run_rate,
        "batsmen": batsmen,
        "bowlers": bowlers,
        "fall": fall_of_wickets,
        "runs_per_over": runs_per_over
    }


def printscoreboard(data):
    print(f"\n{data['team']} - {data['total']}/{data['wickets']} in {data['overs']:.1f} overs")
    print(f"Run Rate: {data['run_rate']:.2f}")
    print("-"*70)

    print("BATTING SCORECARD")
    print(f"{'Batsman':<15}{'Runs':<10}{'Balls':<10}{'SR':<10}")
    for name, stats in data["batsmen"].items():
        if stats["balls"] > 0:
            sr = (stats["runs"]/stats["balls"])*100
            print(f"{name:<15}{stats['runs']:<10}{stats['balls']:<10}{sr:<10.2f}")

    print("\nfall of Wickets:")
    print(", ".join(data["fall"]))

    print("\nBOWLING FIGURES")
    print(f"{'Bowler':<15}{'Overs':<10}{'Runs':<10}{'Wkts':<10}")
    for name, stats in data["bowlers"].items():
        print(f"{name:<15}{stats['overs']:<10}{stats['runs']:<10}{stats['wickets']:<10}")

    print("\nRuns Per Over:")
    for i, runs in enumerate(data["runs_per_over"], start=1):
        print(f"Over {i:>2}: {runs} runs")

    print("="*70)


def decide_winner(team1, team2):
    print("\nMATCH RESULT")
    print("="*70)

    if team1["total"] > team2["total"]:
        margin = team1["total"] - team2["total"]
        print(f"{team1['team']} won by {margin} runs")
    elif team2["total"] > team1["total"]:
        wickets_left = 10 - team2["wickets"]
        print(f"{team2['team']} won by {wickets_left} wickets")
    else:
        print("Match Tied!")

#test 

team1 = simulaledinnings("Peshawar Zalmi")
team2 = simulaledinnings("Islamabad United")

printscoreboard(team1)
printscoreboard(team2)

decide_winner(team1, team2)