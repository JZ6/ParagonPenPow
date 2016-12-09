def pen_or_pow(base_damage: int, scaling: float, armor: int, cxp_power: int, cxp_pen: int, armor_type: str):
    pen_scale = 2
    if armor_type[0].lower() == 'b':
        pen_limit = armor/4;
        pen_scale = 4
    else:
        pen_limit = armor/2

    assert cxp_pen <= pen_limit
    assert cxp_pen + cxp_power <= 60

    dmg_reduction = 100/(100 + armor - pen_scale*cxp_pen)
    pow_increase = scaling*6*cxp_power
    total_dmg = (base_damage + pow_increase)*dmg_reduction
    return total_dmg

#print(pen_or_pow(300, 1.0, 30, 60, 0, 'a'))
