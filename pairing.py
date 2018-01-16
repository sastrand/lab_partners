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
    # This does not work...
    buf, ret = [], []
    for person in class_list:
        for pair in pairs[::-1]:
            if person not in buf:
                if (pair[0] == person and pair[1] not in buf) or (pair[0] not in buf and pair[1] == person):
                    print(pair)
                    class_list.remove(pair)
                    buf.append(pair[0])
                    buf.append(pair[1])
                    break

with open("./class_list.txt") as f:
    class_list = f.read().splitlines()

with open("./rm_pairs.txt") as f:
    rm_pairs = [tuple(l) for l in csv.reader(f)]

first_drv = choose_two(class_list)
first_nav = [p[::-1] for p in first_drv]

[rm_pair(l, rm_pairs) for l in [first_drv, first_nav]]

print("""
 _        ______     _        _______  ______   _______ 
( (    /|(  ___ \   ( \      (  ___  )(  ___ \ (  ____ )
|  \  ( || (   ) )  | (      | (   ) || (   ) )| (    \/
|   \ | || (__/ /   | |      | (___) || (__/ / | (_____ 
| (\ \) ||  __ (    | |      |  ___  ||  __ (  (_____  )
| | \   || (  \ \   | |      | (   ) || (  \ \       ) |
| )  \  || )___) )  | (____/\| )   ( || )___) )/\____) |
|/    )_)|/ \___/   (_______/|/     \||/ \___/ \_______)
                                                        """)
print("length first_drv:", len(first_drv))
print("length first_nav:", len(first_nav))

