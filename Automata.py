###
# Automata.py
# Automata instrument class for Automatunes
# Dylan Everingham
# 9/14/2015
###

import ElementaryRule

# An instance represents one 1D cellular automata
class Automata:

    # Constructor
    def __init__(self, init, rulenum):
        initial = init
        state = init
        width = len(init)
        rule = ElementaryRule.getRule(rulenum)

    # Updates initial condition
    def setInit(self, init):
        initial = init

    # Updates rule
    def setRule(self, rulenum):
        rule = ElementaryRule.getRule(rulenum)

    # Updates current state to next state using rule
    def step(self):
        newstate = state
        for pos in range(width):
            leftCell = state[pos-1] if pos > 0 else 0
            rightCell = state[pos+1] if pos < (width - 1) else 0
            cell = state[pos]
            newstate[pos] = rule[(leftCell,cell,rightCell)]
        state = newstate

    # Resets automata to initial condition
    def reset(self):
        state = initial

    # Plays the sound mapped to the current state
    def play(self):
        # TODO
        return 0

    # Prints current state
    def printState(self):
        for el in state:
            print el,
        print ''
