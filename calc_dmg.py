

def calc_damage(unit1, unit2, elevation="0"):
    """Calculate unit versus unit damage based on armor and attack classes."""
    damage = 0
    for att_cl, att_val in unit1.att_classes:
        for arm_cl, arm_val in unit2.arm_classes:
            if att_cl == arm_cl:
                damage += max(0, att_val - arm_val)

    if elevation == "0":
        ele_mod = 1
    elif elevation == "-":
        ele_mod = 3/4.0
    elif elevation == "+":
        ele_mod = 5/4.0

    damage = round(max(1, damage * ele_mod), 2)

    #  trample where applicable
    # if unit1.blast ...
    # case Elephants 1
    # case Elephants 2
    # case Logistica / Druzhina

    return damage
