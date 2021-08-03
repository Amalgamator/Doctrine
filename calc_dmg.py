

def getDamagePerHit(attacker, defender, elevation="0", distance):
    """Calculate unit versus unit damage based on armor and attack classes."""
    damage = 0
    # find attack classes of the agressor
    # that match armor classes of the defender
    for att_cl, att_val in attacker.attacks:
        for arm_cl, arm_val in defender.armors:
            if att_cl == arm_cl:
                # apply bonus damage
                damage += max(0, att_val - arm_val)

    if elevation == "0":
        # attacker on equal ground
        ele_mod = 1
    elif elevation == "-":
        # attacker on lower ground
        ele_mod = .75
    elif elevation == "+":
        # attacker on higher ground
        ele_mod = 1.25

    damage = round(max(1, damage * ele_mod), 2)

    conditionals = [attacker.blast["attlvl"] <= defender.blast["deflvl"],
                    attacker.r[1]
    if all(conditionals):
        return 5

    #  trample where applicable
    # if unit1.blast ...
    # case Elephants 1
    # case Elephants 2
    # case Logistica / Druzhina

    return damage

def getAttackDelay(animationDuration, FrameDelay, FramesperAngle):
    return animationDuration * 60 * (FrameDelay / FramesperAngle)

def duel(unit1, unit2):
    """Simulate a fight between unit1 and unit2."""
    # set the units apart by the LOS of the highest range unit
    distance = max(unit1.LOS, unit2.LOS)
    while (unit1.HP > 0) and (unit2.HP > 0):
        # HP
        # Speed
        # rof
        # r
        getAttackDelay
        # accuracy
        # projspeed
        # projarc
        # blast
