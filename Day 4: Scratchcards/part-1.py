def main():
    game_numbers = []
    all_games = []
    with open("example-input", "r") as f:
        for line in f: 
            game = line.split(":")
            game_numbers = [int(number.strip().split("|")) for number in game[1:]]
            all_games.append(game_numbers)
    
    results = []

    for game in all_games:
        for game_values in game:
            winning_nums = game_values[0]
            player_nums = game_values[1]
            for num in winning_nums:
           #     results[num] = player_nums.count(num)
                print()

    print(type(all_games[0]))

if __name__ == "__main__":
    main()
