#making the grid
def grid():
    game_field = []
    empty = 0
    for row_index in range(25):
        row = []
        for column in range(50):
            row.append(empty)
        game_field.append(row)
    return game_field