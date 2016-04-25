"""
find the pair of points in 2d space with the smallest distance between them
"""
import itertools
import random as rand
import math
from timing import *
from emailz import send_email

def get_distance(p1, p2):
    delta = []
    for d1, d2 in zip(p1, p2):
        delta += [d1-d2]
    delta_squared = [d ** 2 for d in delta]
    distance = math.sqrt(sum(delta_squared))
    return distance

def min_dist_brute(pairs):
    min_dist, min_pair = 0, ()
    for pair in pairs:
        d = get_distance(*pair)
        if not min_dist:
            min_dist = d
            min_pair = pair
        if d < min_dist:
            min_dist = d
            min_pair = pair
    return min_pair

if __name__ == '__main__':
    message = ""
    for length in [1, 10, 100, 1000, 10000, 100000]:
        try:
            points = [(rand.randint(0, 100), rand.randint(0, 100)) for _ in range(length)]
            pairs = itertools.combinations(points, 2)
            message += "Brute force method took {0}s to find min distance among {1} pairs.\n".format(timethis(min_dist_brute, pairs), length)
        except:
            message += "Failed to find min distance between {0} pairs".format(length)
    message = "At {0}, your process finished.\n".format("$CURRENT_TIME") + message + "Love,\nPythontimerbot"
    send_email("christianfscott@gmail.com", "All done", message)
