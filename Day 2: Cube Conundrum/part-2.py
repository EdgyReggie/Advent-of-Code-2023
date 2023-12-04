def main():
    games = []
    possible_games = []

    with open("input", "r") as f: 
        for line in f: 
            trim = line.split(":")
            game_info = [hand.strip().split(";") for hand in trim[1:]]

            for game in game_info:
                hands = [subset.strip().split(",") for subset in game]
                games.append(hands)

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
