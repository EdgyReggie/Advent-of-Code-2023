def main():
    games = []
    possible_games = []

    result = 0

    with open("input", "r") as f: 
        for line in f: 
            game_info = line.strip().split(";")
            
            # Starting at index one, strip each subset of white space,
            # split by comma, and use list comprehension to create a 
            # new list of lists contaning the colour and count. 
            subsets = [subset.strip().split(",") for subset in game_info[1:]]
            games.append(subsets)

    # This is just a fancy for loop that keeps track of the element and the index
    for i, game in enumerate(games, start=1):
        if possibile_game(game):
            possible_games.append(i)

    print(sum(possible_games))


def possibile_game(game):
    max_red = 12
    max_green = 13 
    max_blue = 14

    for subset in game:
        for colour in subset: 
            count = int(colour.split()[0])
            cube = colour.split()[1]
            if cube == "red" and count > max_red:
                return False
            elif cube == "green" and count > max_green:
                return False
            elif cube == "blue" and count > max_blue:
                return False
    return True


if __name__ == "__main__":
    main()
