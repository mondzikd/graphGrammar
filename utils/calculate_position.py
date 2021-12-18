def calculate_I_pos(pos_a, pos_b, pos_c, pos_d):
    return (
        (pos_a[0] + pos_b[0] + pos_c[0] + pos_d[0])/4,
        (pos_a[1] + pos_b[1] + pos_c[1] + pos_d[1])/4)


def calculate_avg(pos_a, pos_b):
    return (pos_a[0] + pos_b[0]) / 2, (pos_a[1] + pos_b[1]) / 2
