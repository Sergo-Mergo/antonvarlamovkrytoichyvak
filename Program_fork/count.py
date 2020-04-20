def count_win(coef_1, coef_2):
    """This function count sum, which we need to bet for optimal win



        s_1 and s_2 -- variable, which mean bet sum for bet with this coefficients.
        start_sum -- variable, which describe all money that we want to use in bet.
        coef_1 and coef_2 -- variable, which show coefficient in betting site.
    """
    start_sum = float(100)

    s_1 = float(start_sum /(1 + (coef_1 / coef_2)))
    s_2 = float(start_sum - s_1)

    win_1 = s_1 * coef_1 - start_sum
    win_2 = s_2 * coef_2 - start_sum

    return s_1, s_2