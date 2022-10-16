'''Make Chocolate'''

def make_chocolate(small, big, goal):
    big_choco = goal // 5
    if big_choco <= big:
        big_choco = big_choco
    else:
        big_choco = big
    left_choco = goal - (big_choco * 5)
    if small >= left_choco:
        small_choco = left_choco
        return small_choco
    else:
        return -1