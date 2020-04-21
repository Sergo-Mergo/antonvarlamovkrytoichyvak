import search as search


coef_1 = float(input("Введите первый коэффициент"))
coef_2 = float(input("Введите второй коэффициент"))


S_1, S_2  = search.Condition_check(coef_1, coef_2)

print("%.3f"  % S_1,"%.3f" % S_2)