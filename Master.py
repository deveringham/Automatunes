###
# Master.py
# Master track controlling a set of automata
# For Automatunes
# Dylan Everingham
# 9/14/2015
###

# Default to this many measure in the master loop
defaultMeasures = 4

# Deal with his many possible notes per measure
subdivisions = 8

# The default rythm for an automata steps at every possible chance
defaultRhythm = [1] * subdivisions

# Class representing a master loop controlling a set of automata
class Master:
    
    # Constructor
    def __init__(self):
        # Keeps track of current position in the master loop
        pos = 0

        # List of active automata
        automata = []

        # Keeps track of when each automata shold step/play. Has an element for
        # each automata which is a list of length loopLen.
        rhythm = []

        # Keeps track of the number of measures in the master loop
        numMeasures = defaultMeasures

        # Number of subdivisions in the master loop
        loopLen = numMeasures * subdivisions
        
    # Adds new automata
    def addAutomata(self,a):
        automata.append(a)
        rhythm.append(defaultRhythm)

    # Removes automata at certain index
    def removeAutomata(self,i):
        automata.pop(i)

    # Resets all automata
    def reset(self):
        for a in automata:
            a.reset()

    # Steps and plays each automata which should at this point in the loop
    def step(self):
        for i in range(len(automata)):
            a = automata[i]
            if (rhythm[i][pos]):
                a.play()
                a.step()
        pos = pos + 1
        if (pos >= loopLen): pos = 0
