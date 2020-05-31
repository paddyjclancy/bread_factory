
def make_dough(ing1, ing2):
    if ing1 == "water" and ing2 == "flour":
        return "dough"
    elif ing1 == "flour" and ing2 == "water":
        return "dough"
    else:
        return "not dough"

def bake_bread(ing):
    if ing == "dough":
        return "bread"
    else:
        return "not bread"

def make_ww_dough(ing1, ing2):
    if ing1 == "whole wheat flour" and ing2 == "water":
        return "whole wheat dough"
    elif ing1 == "water" and ing2 == "whole wheat flour":
        return "whole wheat dough"
    else:
        return "not whole wheat dough"

def bake_ww_bread(ing):
    if ing == "whole wheat dough":
        return "whole wheat bread"
    else:
        return "not whole wheat bread"

