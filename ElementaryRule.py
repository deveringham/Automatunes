###
# ElementaryRule.py
# Elementary automata rule methods for Automatunes
# Dylan Everingham
# 9/14/2015
###

# Generates elementary rule dictionaries
def elementaryRule(ruleNum):
    # Returns 0 if rule number is not in bounds
    if ruleNum < 0 or ruleNum > 255: return 0

    # Get 8 bit binary representation of rulenum
    b = '{0:08b}'.format(ruleNum)
    # Convert to list so we can pop from it
    b = list(b)

    # Use that to get rule
    rule = {(x,y,z):int(b.pop()) for x in [0,1] for y in [0,1] for z in [0,1]}

    return rule
