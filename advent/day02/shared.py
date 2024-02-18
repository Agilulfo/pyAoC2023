def decode(line):
    [game_info, game_play] = line[:-1].split(":")
    game_number = int(game_info[5:])
    rounds = game_play.split(";")
    decoded_rounds = []

    for round in rounds:
        red = 0
        green = 0
        blue = 0
        groups = round.split(",")

        for group in groups:
            [_, amount, color] = group.split(" ")
            if color == "red":
                red = int(amount)
            elif color == "green":
                green = int(amount)
            else :
                blue = int(amount)
        decoded_rounds.append(
            (red, green, blue)
        )

    return (game_number, decoded_rounds)
