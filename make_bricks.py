def make_bricks(small, big, goal):
    if small * 1 + big * 5 == goal :
      return True
    elif small * 1 + big * 5 > goal :
      if goal % 5 == 0 :
        if small % 5 == 0:
          if big * 5 + small * 1>= goal :
            return True
          else :
            return False
        else:
          if big * 5 >= goal:
            return True
          else:
            return False
      else:
        if big > 0 and big * 5 > goal:
          banyak_big =goal // 5
          sisa_diperlukan = goal - banyak_big * 5
          if small * 1 >= sisa_diperlukan :
            return True
          else:
            return False
        elif big > 0 and big * 5 < goal:
          sisa_diperlukan = goal - big * 5
          if small * 1 >= sisa_diperlukan :
            return True
          else:
            return False
        else:
          if small * 1 >= goal:
            return True
          else:
            return False
    else:
      return False
        