import csv

def choose_two(class_list):
        ret = []
        for p1 in range(len(class_list)):
                for p2 in range(p1+1,len(class_list)):
                        ret.append((class_list[p1],class_list[p2]))
        return ret

def rm_pair(pairs, rm_pairs):
    for p in rm_pairs: 
        try:
            pairs.remove(p)
        except:
            pass

def rm_person_by_pos(pairs, name, position):
    for p in pairs:
        if p[0] == name and position == "drv":
            pairs.remove(p)
        elif p[1] == name and position == "nav":
            pairs.remove(p)

def lab_pairs(pairs, class_list):
    here = []
    for person in class_list:
        for pair in pairs:
            if person not in here:
                if (pair[0] == person and pair[1] not in here) or (pair[0] not in here and pair[1] == person):
                    f.write(str(pair) + "\n")
                    pairs.remove(pair)
                    here.append(pair[0])
                    here.append(pair[1])
                    break

with open("./class_list.txt") as f:
    class_list = f.read().splitlines()

with open("./rm_pairs.txt") as f:
    rm_pairs = [tuple(l) for l in csv.reader(f)]

f = open("output.txt", "w")

first_drv = choose_two(class_list)
first_drv = first_drv[::-1]
first_nav = [p[::-1] for p in first_drv]

[rm_pair(l, rm_pairs) for l in [first_drv, first_nav]]

f.write("""
 _        ______     _        _______  ______   _______ 
( (    /|(  ___ \   ( \      (  ___  )(  ___ \ (  ____ )
|  \  ( || (   ) )  | (      | (   ) || (   ) )| (    \/
|   \ | || (__/ /   | |      | (___) || (__/ / | (_____ 
| (\ \) ||  __ (    | |      |  ___  ||  __ (  (_____  )
| | \   || (  \ \   | |      | (   ) || (  \ \       ) |
| )  \  || )___) )  | (____/\| )   ( || )___) )/\____) |
|/    )_)|/ \___/   (_______/|/     \||/ \___/ \_______)
                                                        """)
for week in range(2,11):
    f.write("\n\n---- Week {} ----\n".format(week))
    f.write("\n-- Tuesday --\n".format(week))
    lab_pairs(first_drv, class_list)
    f.write("\n-- Thursday --\n".format(week))
    lab_pairs(first_nav, class_list)

f.close()
