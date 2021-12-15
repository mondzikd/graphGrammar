def calculate_I_pos(pos):
    return (
        (pos[1][0] + pos[2][0] + pos[3][0] + pos[4][0])/4,
        (pos[1][1] + pos[2][1] + pos[3][1] + pos[4][1])/4)


def calculate_e_pos(pos):
    return (pos[1][0] + pos[2][0]) / 2, pos[1][1] + pos[2][1] * 0.6
