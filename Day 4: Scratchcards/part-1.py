def main():
    game_numbers = []
    all_games = []

    with open("example-input", "r") as f:
        for line in f: 
            game = line.split(":")
            game_numbers = [number.strip().split("|") for number in game[1:]]
            for game_set in game_numbers:
                for indv_num in game_set:
                    nums = indv_num.split(" ")
                    c = nums.count("")
                    for i in range(c):
                        nums.remove("")
                    print(nums)
            all_games.append(game_numbers)
    
    results = []

    for game in all_games:
        for game_values in game:
            winning_nums = [int(num) for num in game_values[0] if num.strip()]
            player_nums = game_values[1]
            for num in winning_nums:
                results[num] = player_nums.count(num)

if __name__ == "__main__":
    main()
