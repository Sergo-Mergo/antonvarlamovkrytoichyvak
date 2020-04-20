import count as count



def Condition_check(coef_1, coef_2):
    """This function check condition to count win summ



        coef_1 and coef_2 -- variable, which show coefficient in betting site.
        a - local variable -- main condition.
    """
    a = 1/(coef_1) + 1/(coef_2)

    if (a < 0.99999):
        s_1, s_2 = count.count_win(coef_1, coef_2)

    return s_1, s_2