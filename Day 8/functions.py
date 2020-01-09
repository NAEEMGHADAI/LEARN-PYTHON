import sys
sys.setrecursionlimit(1500)

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

def printFunction(the_list):
    for p in planets:
        if isinstance(p, list):
            printFunction(p)
        else:
            print(p)

printFunction(planets)
