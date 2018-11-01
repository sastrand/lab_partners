# https://stackoverflow.com/questions/28748520/creating-random-pairs-from-lists

import random


def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)


if __name__ == "__main__":

    with open("./class_list.txt") as f:
        lst = f.read().splitlines()

    if len(lst) % 2 != 0:
        lst.append("--")

    pairs = []
    while lst:
        rand1 = pop_random(lst)
        rand2 = pop_random(lst)
        pair = rand1, rand2
        pairs.append(pair)

    formatted_pairs = ["{:8} {:8}".format(p[0], p[1]) for p in pairs]

    print("\n{:*^30}".format(" Random Lab Partners "))
    [print("{:^30}".format(p)) for p in formatted_pairs]
    print("\n")
