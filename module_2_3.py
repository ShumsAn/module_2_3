
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
f = 0
while f < len(my_list) :
    if my_list[f] > 0:
            print(my_list[f])
            f = f + 1
    elif my_list[f] == 0:
            f = f + 1
    else:
        break





