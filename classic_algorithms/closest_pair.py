"""
find the pair of points in 2d space with the smallest distance between them
"""
import itertools
import random as rand
import math
from timing import *
from emailz import send_email
from datetime import datetime

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

def right_pad(s, l):
    return (s + ' ' * (l - len(s))) if len(s) < l else s

if __name__ == '__main__':
    print("running... ")
    message = ""
    times = []
    now = datetime.now().strftime('%H:%M')
    for length in [1, 10, 100, 1000, 10000, 100000]:
        print(right_pad("matching %d pairs... " % length, 25), end="")
        points = [(rand.randint(0, 100), rand.randint(0, 100)) for _ in range(length)]
        pairs = itertools.combinations(points, 2)
        time = timethis(min_dist_brute, pairs)
        message += "brute force method took %.5fs to find min distance among %d pairs\n\n" % ((time, length))
        print("OK (%.5fs)" % time)
    then = datetime.now().strftime('%H:%M')
    message = "%sstarted at %s and finished at %s.\n\nlove,\npythontimerbot" % (message, now, then)
    send_email("christianfscott@gmail.com", "testing 123", message)
    print("email sent to christianfscott@gmail.com")
