from CalculatorBase import pen_or_pow
import matplotlib.pyplot as plt

def pow_pen_balance(base_damage, scaling, armor, current_cxp, armor_type: str):
    assert current_cxp <= 60

    if armor_type[0].lower() == 'b':
        pen_limit = armor/4;
        armor_ts = " basic"
    else:
        pen_limit = armor/2
        armor_ts = " ability"

    max_damage = 0
    max_pen = 0
    max_pow = 0
    for pen_cxp in range(0, int(pen_limit)+1):
        pow_cxp = current_cxp - pen_cxp
        current_dmg = pen_or_pow(base_damage, scaling, armor, pow_cxp, pen_cxp, armor_type)
        if max_damage < current_dmg:
            max_damage = current_dmg
            max_pen = pen_cxp
            max_pow = pow_cxp

    return "Maximum damage for an attack with "+ str(base_damage) + " base damage and " + str(scaling) + " scaling at " + str(current_cxp) + " cxp is " + str(max_damage) + " from " + str(max_pen) + " cxp of pen and "+ str(max_pow) + " cxp of power on an enemy with " + str(armor) + armor_ts + " armor."


print(pow_pen_balance(60, 0.7, 20, 60, 'a'))
