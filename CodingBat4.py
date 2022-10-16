'''Close Far'''
def close_far (a , b , c):
    scenario_1 = abs (b - a) <= 1
    scenario_2 = abs (c - a) <= 1
    scenario_1_negation = not scenario_1
    scenario_2_negation = not scenario_2

    if (scenario_1 and scenario_2_negation) or (scenario_2 and scenario_1_negation):
        return True
    else:
        return False

print(close_far(1,2,3))