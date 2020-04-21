import search as search


list_1=[]
list_2=[]

list_1, a = search.Get_good_position()

for i in range(a):
    list_2 = list_1[i]
    for j in 1,2,3:
        number_of_string, summ_1, summ_2 = list_2[0], list_2[1], list_2[2]
    print(int(number_of_string), float(summ_1), float(summ_2))