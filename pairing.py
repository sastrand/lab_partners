import csv

with open("./class_list.txt") as f:
    class_list = f.read().splitlines()

f = open("output.txt", "w")

class_list_a = class_list[:len(class_list)//2]
class_list_b = class_list[len(class_list)//2:]

def get_weeks_pairs(cl_a, cl_b):
    cl_a.append(cl_b[-1])
    del cl_b[-1]
    cl_b.insert(0, cl_a[0])
    del cl_a[0]
    return zip(cl_a, cl_b)

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

for week in range(3,20):
    f.write("\n\n---- Rotation {} ----\n\n".format(week))
    for p in get_weeks_pairs(class_list_a, class_list_b):
        f.write(str(p) + "\n")

f.close()

