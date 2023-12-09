def main():
    all_games = []

    do_file_io(all_games)


        
    print(sum(calc_result(all_games)))

def do_file_io(all_games):
    with open("input", "r") as f:
        game_numbers = []
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

def calc_result(all_games):
    results = []

    for game in all_games:
        winning_nums = game[0]
        player_nums = game[1]
        count = 0
        result = 0
        
        for num in winning_nums:
            count += player_nums.count(num)
        
        for i in range(1, count + 1):
            if result == 0: 
                result = i
            else:
                result *= 2

        results.append(result)

    return results

if __name__ == "__main__":
    main()
