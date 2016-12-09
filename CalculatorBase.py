def pen_or_pow(base: int, scaling: float, armor: int, cxp_power: int, cxp_pen: int):
    assert cxp_pen + cxp_power == 60
    dmg_reduction = 100/(100 + armor - 4*cxp_pen)
    pow_increase = scaling*6*cxp_power
    total_dmg = (base + pow_increase)*dmg_reduction
    return total_dmg

pen_or_pow(300, 1.0, 30, 60,0)
