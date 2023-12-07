def main():
    game_numbers = []
    total_numbers = []
    with open("example-input", "r") as f:
        for line in f: 
            game = line.split(":")
            game_numbers = [number.strip().split("|") for number in game[1:]]
            total_numbers.append(game_numbers)

    print(total_numbers)

if __name__ == "__main__":
    main()
