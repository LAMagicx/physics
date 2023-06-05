"""
File contains function that are used for vector operations
here a vector is a np array [x,y]
Todo:
    add support for z
"""
import numpy as np


def init(x, y=None):
    return np.array([float(x), float(y)])


def random(a=0, b=1):
    return np.random.uniform(a, b, size=(2,))


def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def pdot(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


def norm(v):
    return np.sqrt(v[0] ** 2 + v[1] ** 2)


def normalise(v):
    n = norm(v)
    if n == 0:
        return v
    return init(v[0] / n, v[1] / n)


def limit(v, m):
    if norm(v) > m:
        return normalise(v) * m
    return v


def dist(v1, v2):
    return norm(v1 - v2)


def dist_quick(v1, v2):
    """removes the sqrt from the dist"""
    v = v1 - v2
    return v[0] ** 2 + v[1] ** 2
