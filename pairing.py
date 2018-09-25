import csv
from itertools import combinations

def choose_two(class_list):
    return list(combinations(class_list, 2))

def lab_pairs(pairs, class_list):
    print pairs
    print len(pairs)
    print class_list
    accounted_for = set()
    i = 0
    for student in class_list:
        while student not in accounted_for:
            if (pairs[i][0] == student and pairs[i][1] not in accounted_for) or (pairs[i][0] not in accounted_for and pairs[i][1] == student):
                f.write(str(pairs[i]) + "\n")
                accounted_for.add(pairs[i][0])
                accounted_for.add(pairs[i][1])
                #  pairs.remove(pairs[i])
            if i >= len(pairs)-1:
                i = 0
            else:
                i = i + 1

with open("./class_list.txt") as f:
    class_list = f.read().splitlines()

f = open("output.txt", "w")

first_drv = choose_two(class_list)
first_nav = [p[::-1] for p in first_drv]
class_list = class_list[::-1]

f.write("""
 _        ______     _        _______  ______   _______ 
( (    /|(  ___ \   ( \      (  ___  )(  ___ \ (  ____ )
|  \  ( || (   ) )  | (      | (   ) || (   ) )| (    \/
|   \ | || (__/ /   | |      | (___) || (__/ / | (_____ 
| (\ \) ||  __ (    | |      |  ___  ||  __ (  (_____  )
| | \   || (  \ \   | |      | (   ) || (  \ \       ) |
| )  \  || )___) )  | (____/\| )   ( || )___) )/\____) |
|/    )_)|/ \___/   (_______/|/     \||/ \___/ \_______)
                                                        \n""")

lab_pairs(first_drv, class_list)

#  for week in range(2,20):
    #  f.write("\n\n---- Week {} ----\n".format(week))
    #  f.write("\n-- Tuesday --\n")
    #  f.write("'DRIVER','NAVIGATOR'\n")
    #  lab_pairs(first_drv, class_list)
    #  f.write("\n-- Thursday --\n")
    #  f.write("'DRIVER','NAVIGATOR'\n")
    #  lab_pairs(first_nav, class_list)

f.close()

