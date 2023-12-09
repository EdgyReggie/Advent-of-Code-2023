def main():
    game_numbers = []
    all_games = []

    with open("example-input", "r") as f:
        for line in f: 
            game = line.split(":")
            game_numbers = [number.strip().split("|") for number in game[1:]]
            for game_set in game_numbers:
                working_list = []
                for indv_num in game_set:
                    nums = indv_num.split(" ")
                    c = nums.count("")
                    for i in range(c):
                        nums.remove("")
                    working_list.append(nums)
                all_games.append(working_list)

    print(all_games)

    results = []

    for game in all_games:
        for game_values in game:
            winning_nums = game_values[0]
            player_nums = game_values[1]
            #for num in winning_nums:
            #    results[num] = player_nums.count(num)

if __name__ == "__main__":
    main()
