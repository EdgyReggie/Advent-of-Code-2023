def main():
    games = []
    powers = []

    with open("input", "r") as f: 
        for line in f: 
            trim = line.split(":")
            game_info = [hand.strip().split(";") for hand in trim[1:]]

            for game in game_info:
                hands = [subset.strip().split(",") for subset in game]
                games.append(hands)

    for game in games: 
        game_powers(game, powers)
            
    print(sum(powers))

def game_powers(game, powers):
    min_red = 0
    min_green = 0
    min_blue = 0

    for subset in game:
        for colour in subset: 
            count = int(colour.split()[0])
            cube = colour.split()[1]

            if cube == "red" and count > min_red: 
                min_red = count
            elif cube == "green" and count > min_green:
                min_green = count
            elif cube == "blue" and count > min_blue: 
                min_blue = count
    powers.append(min_red * min_green * min_blue)



if __name__ == "__main__":
    main()
