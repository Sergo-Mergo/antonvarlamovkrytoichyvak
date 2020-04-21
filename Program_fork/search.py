import count as count



def Condition_check(coef_1, coef_2):
    """This function check condition to count win summ



        coef_1 and coef_2 -- variable, which show coefficient in betting site.
        a - local variable -- main condition.
    """
    a = 1/(coef_1) + 1/(coef_2)
    s_1, s_2 = 0, 0

    if (a < 0.99999):
        s_1, s_2  = count.count_win(coef_1, coef_2)


    return s_1, s_2

def Input_data(name_of_file):

    array_of_string=[]

    file = open(name_of_file, 'r')

    a = 0

    for line in file:
        a = a + 1
        array_of_string.append(line)

    file.close()

    return array_of_string, a


def Get_good_position():
    name = input("Введите имя файла в формате name.txt: ")
    file, a = Input_data(name)

    number=[]
    list=[]
    good_position=[]
    final_number = 0

    for i in range(a):
        number.append(file[i].split())
        list=number[i]

        for i in 0,1,2:
            number_of_string, C_1, C_2 = list[0],list[1],list[2]
            summ_1, summ_2 = Condition_check(float(C_1), float(C_2))

        if ((summ_1 != 0) and (summ_2 != 0)):
            good_position.append([number_of_string, summ_1, summ_2])
            final_number = final_number + 1

    return good_position, final_number